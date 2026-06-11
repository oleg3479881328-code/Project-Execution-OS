# AWS Wan Smoke Test Runbook — Reels Factory MVP

Date: 2026-06-10 (corrected)
Target: One 3-second 480p Wan Image-to-Video generation on AWS GPU
Author: Infrastructure executor

---

## Before You Start

- You have AWS credits: **$74.57** (expires 2026-10-04)
- GPU quota is approved: **4 vCPU** (g4dn.xlarge / g5.xlarge / g6.xlarge fit exactly)
- Region: **us-east-2** (Ohio)
- Budget for this test: **~$2-4** (2-3 hours of runtime)
- **Do not leave the instance running after the test.**

## Important Model Note

After verifying the official Wan2.1 repository (https://github.com/Wan-Video/Wan2.1), the available Image-to-Video models are:

- **Wan2.1-I2V-14B-480P** (only I2V variant — no I2V-1.3B exists)
- **Wan2.1-I2V-14B-720P**

The 14B model requires ~18-22 GB VRAM at FP16. This affects instance selection (see below).

## Instance Selection

**First launch candidate: g5.xlarge** (4 vCPU, 24 GB VRAM A10G, $1.006/hr)

**Why not g4dn.xlarge?** g4dn.xlarge has only 16 GB VRAM, which may be insufficient for I2V-14B at FP16. g5.xlarge (24 GB VRAM) provides safe headroom.

**Alternative:** If you want to try the cheaper g4dn.xlarge first, use the FP8 quantized model from Kijai (https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled) with block swapping enabled. If it fails (OOM), terminate and relaunch on g5.xlarge.

---

## Step 1: Launch the EC2 Instance

### Via AWS Console (recommended for first time)

1. Open EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
2. Click **Launch instance**
3. Name: `reels-factory-smoke-test`
4. **AMI:** Select **Deep Learning AMI GPU PyTorch 2.x (Ubuntu 22.04)**
   - Search for "Deep Learning AMI GPU" in the AMI catalog
   - Select the latest Ubuntu 22.04 version
5. **Instance type:** `g5.xlarge` (4 vCPU, 24 GB VRAM) — or `g4dn.xlarge` if testing FP8
6. **Key pair:** Select an existing key pair or create a new one
   - If creating: "Create new key pair" → name it `reels-factory-key` → download the `.pem` file
7. **Network settings:**
   - VPC: default
   - Subnet: any
   - **Security group:** Create new
     - Allow **SSH (22/TCP)** from **your IP only** (e.g., `147.0.42.138/32`) — do NOT use 0.0.0.0/0
     - Allow **Custom TCP (8188)** from **your IP only** for ComfyUI web interface, OR use SSH tunneling (see Step 5)
8. **Storage:** Set root volume to **50 GB gp3** (30 GB is insufficient for DLAMI + models + dependencies)
9. **Advanced details:** Leave defaults
10. **Summary:** Review and click **Launch instance**

### Via AWS CLI (if you prefer)

```bash
# Create security group with IP restriction (replace with your IP)
aws ec2 create-security-group --group-name reels-factory-smoke-sg --description "Reels Factory smoke test SG" --region us-east-2

# Add SSH from your IP only (REPLACE 147.0.42.138 with your actual IP)
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 22 --cidr 147.0.42.138/32 --region us-east-2

# Add ComfyUI port from your IP only (or skip and use SSH tunneling)
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 8188 --cidr 147.0.42.138/32 --region us-east-2

# Find the latest Deep Learning AMI GPU PyTorch 2.x
aws ec2 describe-images --region us-east-2 --owners amazon --filters "Name=name,Values=*Deep Learning AMI GPU PyTorch*" --query "Images[*].[ImageId,Name,CreationDate]" --output table

# Launch instance (replace ami-xxx with the actual AMI ID, use g5.xlarge or g4dn.xlarge)
aws ec2 run-instances --image-id ami-xxx --instance-type g5.xlarge --key-name reels-factory-key --security-groups reels-factory-smoke-sg --block-device-mappings "[{\"DeviceName\":\"/dev/sda1\",\"Ebs\":{\"VolumeSize\":50,\"VolumeType\":\"gp3\"}}]" --region us-east-2
```

### ⏱ Expected setup time: 5 minutes

---

## Step 2: Connect to the Instance

```bash
# Make your key file readable only by you (Linux/Mac)
chmod 400 reels-factory-key.pem

# SSH into the instance (replace with your instance's public IP)
ssh -i reels-factory-key.pem ubuntu@<INSTANCE_PUBLIC_IP>
```

**Where to find the public IP:**
- EC2 Console → Instances → select your instance → copy **Public IPv4 address**

### ⏱ Expected time: 1 minute

---

## Step 3: Install ComfyUI and WanVideoWrapper

Run these commands on the instance:

```bash
# Update system
sudo apt-get update -y

# Install git and other dependencies
sudo apt-get install -y git wget unzip

# Clone ComfyUI
cd ~
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Install Python dependencies
pip install -r requirements.txt

# Install ComfyUI Manager (optional but recommended)
cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
cd ..

# Install WanVideoWrapper
cd custom_nodes
git clone https://github.com/kijai/ComfyUI-WanVideoWrapper.git
cd ..

# Install WanVideoWrapper dependencies
pip install -r custom_nodes/ComfyUI-WanVideoWrapper/requirements.txt
```

### ⏱ Expected time: 5-10 minutes

---

## Step 4: Download the Wan I2V Model

**Important:** The ComfyUI-WanVideoWrapper uses a specific model format from Kijai's HuggingFace repo, NOT the official Wan-AI checkpoints directly.

### Model folder structure (ComfyUI-WanVideoWrapper):

| Component | Folder | Source |
|---|---|---|
| Main transformer model | `ComfyUI/models/diffusion_models/` | https://huggingface.co/Kijai/WanVideo_comfy |
| Text encoder | `ComfyUI/models/text_encoders/` | https://huggingface.co/Kijai/WanVideo_comfy |
| CLIP vision | `ComfyUI/models/clip_vision/` | https://huggingface.co/Kijai/WanVideo_comfy |
| VAE | `ComfyUI/models/vae/` | https://huggingface.co/Kijai/WanVideo_comfy |
| FP8 scaled models (alternative) | `ComfyUI/models/diffusion_models/` | https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled |

### Option A: FP16 models (recommended for g5.xlarge with 24 GB VRAM)

```bash
# Install huggingface-cli if not present
pip install huggingface-hub

# Create model directories
mkdir -p ~/ComfyUI/models/diffusion_models
mkdir -p ~/ComfyUI/models/text_encoders
mkdir -p ~/ComfyUI/models/clip_vision
mkdir -p ~/ComfyUI/models/vae

# Download models from Kijai's repo
# Note: Check the actual filenames at https://huggingface.co/Kijai/WanVideo_comfy/tree/main
# Typical files needed for I2V:
huggingface-cli download Kijai/WanVideo_comfy --local-dir ./ComfyUI/models/diffusion_models --include "wan2.1_i2v_14b*"
huggingface-cli download Kijai/WanVideo_comfy --local-dir ./ComfyUI/models/text_encoders --include "*t5*"
huggingface-cli download Kijai/WanVideo_comfy --local-dir ./ComfyUI/models/clip_vision --include "*clip*"
huggingface-cli download Kijai/WanVideo_comfy --local-dir ./ComfyUI/models/vae --include "*vae*"
```

### Option B: FP8 scaled models (try this for g4dn.xlarge with 16 GB VRAM)

```bash
# FP8 models use less VRAM at the cost of slight quality loss
huggingface-cli download Kijai/WanVideo_comfy_fp8_scaled --local-dir ./ComfyUI/models/diffusion_models --include "wan2.1_i2v_14b*"
```

### ⏱ Expected download time: 10-30 minutes (I2V-14B is ~30 GB)

---

## Step 5: Start ComfyUI

### Option A: Direct web access (if you opened port 8188 to your IP)

```bash
cd ~/ComfyUI
python main.py --listen 0.0.0.0 --port 8188
```

Then open `http://<INSTANCE_PUBLIC_IP>:8188` in your browser.

### Option B: SSH tunneling (recommended — no open ports needed)

On your local machine:
```bash
ssh -i reels-factory-key.pem -L 8188:localhost:8188 ubuntu@<INSTANCE_PUBLIC_IP>
```

Then on the instance:
```bash
cd ~/ComfyUI
python main.py --listen 127.0.0.1 --port 8188
```

Then open `http://localhost:8188` in your browser.

### ⏱ Expected time: 30 seconds

---

## Step 6: Load the Wan I2V Workflow

The ComfyUI-WanVideoWrapper includes example workflows. Check the exact path:

```bash
# List example workflows
ls ~/ComfyUI/custom_nodes/ComfyUI-WanVideoWrapper/example_workflows/
```

Look for files named `wan_i2v*.json` or similar. Load one in ComfyUI via **Load** button.

**If no example workflow exists yet**, the minimal I2V workflow needs these nodes (exact names from the wrapper):
- **LoadImage** — your input start image
- **LoadWanVideoModel** (or similar) — loads the I2V model from `diffusion_models/`
- **WanVideoI2V** (or similar) — the I2V generation node
- **VAEDecode** — decode the latent to video
- **VideoCombine** — combine frames into a video file

**Note:** Exact node names must be verified from the installed wrapper. After installation, right-click in ComfyUI → "Add Node" → search for "Wan" to see available nodes.

---

## Step 7: Prepare the Input Image

1. Generate a start image using ChatGPT (as decided in the project plan)
2. Save it as a PNG file
3. Resolution: 480p (854x480 or similar)
4. In ComfyUI, use the **LoadImage** node to load your image

---

## Step 8: Configure Generation Settings

Settings for the I2V node (approximate — exact parameter names depend on the wrapper version):

| Parameter | Value |
|---|---|
| Model | Wan2.1-I2V-14B-480P |
| Width | 854 |
| Height | 480 |
| Length | 81 frames (~3 seconds at 24fps) |
| Guidance Scale | 5.0 |
| Steps | 40 (I2V-14B uses 40 steps per official docs) |
| Seed | 42 (fixed for reproducibility) |

**If using g4dn.xlarge with FP8:** Enable block swapping in the model loader node. Start with 20/40 blocks offloaded to RAM.

---

## Step 9: Generate!

1. Click **"Queue Prompt"** in ComfyUI
2. Wait for the generation to complete
3. The output video will appear in the preview node

### ⏱ Expected generation time: **UNKNOWN — not yet validated on this hardware**

The official Wan2.1 benchmarks show:
- I2V-14B on a single A100 (80 GB): ~40 seconds for 480p
- I2V-14B on a single 4090 (24 GB) with offloading: several minutes
- On g5.xlarge (A10G): estimate **3-10 minutes** (unvalidated)
- On g4dn.xlarge (T4) with FP8 + swapping: estimate **10-30 minutes** (unvalidated)

Generation time must be measured during the actual test.

---

## Step 10: Download the Output

**Option A: Via ComfyUI web interface**
- Right-click on the output video → "Save" or use the download button

**Option B: Via SCP from your local machine**
```bash
scp -i reels-factory-key.pem ubuntu@<INSTANCE_PUBLIC_IP>:~/ComfyUI/output/*.mp4 .
```

**Option C: Via S3 (if you have an S3 bucket)**
```bash
aws s3 cp ~/ComfyUI/output/ s3://your-bucket/reels-factory-smoke-test/ --recursive
```

---

## Step 11: Record Results

Fill in the COST_TRACKING_TEMPLATE.md with your actual measurements.

---

## Step 12: Clean Up — CRITICAL

**Do not skip this step. GPU instances are expensive.**

### Terminate the instance:

```bash
# Via AWS CLI
aws ec2 terminate-instances --instance-ids i-xxxxxxxx --region us-east-2

# Via AWS Console
# EC2 → Instances → select instance → Instance State → Terminate → Confirm
```

### Verify cleanup:

1. **EC2 Instances:** Check that no GPU instances are running
   - https://console.aws.amazon.com/ec2/home?region=us-east-2#Instances:
2. **EBS Volumes:** Check that no orphaned volumes remain
   - https://console.aws.amazon.com/ec2/home?region=us-east-2#Volumes:
3. **Elastic IPs:** Release any unused Elastic IPs
   - https://console.aws.amazon.com/ec2/home?region=us-east-2#Addresses:
4. **Snapshots:** Delete any temporary snapshots
   - https://console.aws.amazon.com/ec2/home?region=us-east-2#Snapshots:
5. **Security Groups:** Delete the temporary security group
   - https://console.aws.amazon.com/ec2/home?region=us-east-2#SecurityGroups:

### ⏱ Expected cleanup time: 2 minutes

---

## Troubleshooting

### "CUDA out of memory"
- Use FP8 quantized model (Kijai/WanVideo_comfy_fp8_scaled)
- Enable block swapping in the model loader (offload 20-30 blocks)
- Reduce frame count (try 41 frames instead of 81)
- Reduce resolution (try 640x360)
- If on g4dn.xlarge and still OOM, terminate and relaunch on g5.xlarge

### "Cannot connect to ComfyUI"
- If using direct access: check security group rules (port 8188 must be open to your IP)
- If using SSH tunnel: check the tunnel is active
- Check that ComfyUI is running (`ps aux | grep python`)
- Check the instance's public IP hasn't changed

### "Model download is too slow"
- Use `screen` or `tmux` to keep the download running in the background
- The I2V-14B model is ~30 GB — expect 10-30 minutes download time

### "SSH connection refused"
- Wait 2-3 minutes after launching the instance (it takes time to boot)
- Check security group (port 22 must be open to your IP)
- Check that you're using the correct username (`ubuntu` for Ubuntu AMIs)

---

## Fallback Route: RunPod

If AWS setup becomes too cumbersome:

1. Go to https://www.runpod.io
2. Fund minimum **$10** (custom amount)
3. Select a GPU pod with 24+ GB VRAM (RTX 3090, RTX 4090, or A5000)
4. Use the Community Cloud template "ComfyUI" (pre-installed)
5. Upload your image and run the same Wan I2V workflow
6. Terminate the pod after the test

---

## Direct Links

- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
- Launch Instance: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- ComfyUI: https://github.com/comfyanonymous/ComfyUI
- ComfyUI-WanVideoWrapper: https://github.com/kijai/ComfyUI-WanVideoWrapper
- Wan2.1 GitHub: https://github.com/Wan-Video/Wan2.1
- Wan models (official): https://huggingface.co/Wan-AI
- WanVideo ComfyUI models (Kijai): https://huggingface.co/Kijai/WanVideo_comfy
- WanVideo FP8 scaled (Kijai): https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
