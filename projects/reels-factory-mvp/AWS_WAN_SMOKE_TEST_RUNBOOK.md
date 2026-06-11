# AWS Wan Smoke Test Runbook — Reels Factory MVP

Date: 2026-06-10 (final)
Target: One 3-second 480p Wan Image-to-Video generation on AWS GPU
Author: Infrastructure executor

---

## Before You Start

- AWS credits: **$74.57** (expires 2026-10-04)
- GPU quota: **4 vCPU** (approved)
- Region: **us-east-2** (Ohio)
- Budget: **~$3-6** (2-3 hours)
- **Do not leave the instance running after the test.**

## Canonical First-Run Route

| Decision | Value |
|---|---|
| **Instance** | **g5.xlarge** (4 vCPU, 24 GB VRAM A10G, $1.006/hr) |
| **Model** | Wan2.1-I2V-14B-480P (FP16, Diffusers format) |
| **Source** | https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P |
| **Workflow** | `wanvideo_2_1_14B_I2V_example_03.json` |
| **Workflow source** | https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_2_1_14B_I2V_example_03.json |
| **Root volume** | **100 GB gp3** |
| **Security** | Source-IP restriction only (no 0.0.0.0/0) |

**Why g5.xlarge?** I2V-14B requires ~18-22 GB VRAM at FP16. g4dn.xlarge (16 GB) is insufficient. g5.xlarge (24 GB A10G) provides safe headroom. At $1.006/hr, a 3-hour test costs ~$3 — well within the $74.57 credit budget.

---

## Preflight Checklist (complete before launching EC2)

- [ ] I have my public IP ready for security group restriction: _______________
- [ ] I have an SSH key pair or will create one during launch
- [ ] I know the exact workflow file: `wanvideo_2_1_14B_I2V_example_03.json`
- [ ] I know the exact model: `Wan-AI/Wan2.1-I2V-14B-480P` (Diffusers format)
- [ ] I will use **g5.xlarge** (not g4dn.xlarge)
- [ ] I will set root volume to **100 GB gp3**
- [ ] I will restrict SSH and ComfyUI ports to my IP only
- [ ] I have the cleanup links bookmarked (see Step 12)

---

## Step 1: Launch the EC2 Instance

### Via AWS Console

1. Open EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
2. Click **Launch instance**
3. Name: `reels-factory-smoke-test`
4. **AMI:** Select **Deep Learning AMI GPU PyTorch 2.x (Ubuntu 22.04)**
   - Search for "Deep Learning AMI GPU" in the AMI catalog
   - Select the latest Ubuntu 22.04 version
5. **Instance type:** `g5.xlarge`
6. **Key pair:** Select existing or create new → name it `reels-factory-key`
7. **Network settings:**
   - Security group: Create new
   - **SSH (22/TCP):** from **your IP only** (e.g., `147.0.42.138/32`)
   - **Custom TCP (8188):** from **your IP only** (for ComfyUI)
8. **Storage:** Set root volume to **100 GB gp3**
9. Click **Launch instance**

### Via AWS CLI

```bash
# Create security group
aws ec2 create-security-group --group-name reels-factory-smoke-sg --description "Reels Factory smoke test SG" --region us-east-2

# Add SSH from your IP only (REPLACE with your actual IP)
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 22 --cidr YOUR_IP/32 --region us-east-2

# Add ComfyUI port from your IP only
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 8188 --cidr YOUR_IP/32 --region us-east-2

# Find the latest DLAMI
aws ec2 describe-images --region us-east-2 --owners amazon --filters "Name=name,Values=*Deep Learning AMI GPU PyTorch*" --query "Images[*].[ImageId,Name,CreationDate]" --output table

# Launch (replace ami-xxx)
aws ec2 run-instances --image-id ami-xxx --instance-type g5.xlarge --key-name reels-factory-key --security-groups reels-factory-smoke-sg --block-device-mappings "[{\"DeviceName\":\"/dev/sda1\",\"Ebs\":{\"VolumeSize\":100,\"VolumeType\":\"gp3\"}}]" --region us-east-2
```

---

## Step 2: Connect via SSH

```bash
chmod 400 reels-factory-key.pem
ssh -i reels-factory-key.pem ubuntu@<INSTANCE_PUBLIC_IP>
```

---

## Step 3: Install ComfyUI + WanVideoWrapper

```bash
sudo apt-get update -y && sudo apt-get install -y git wget unzip

cd ~
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt

# Install WanVideoWrapper
cd custom_nodes
git clone https://github.com/kijai/ComfyUI-WanVideoWrapper.git
cd ..
pip install -r custom_nodes/ComfyUI-WanVideoWrapper/requirements.txt
```

---

## Step 4: Download the Wan I2V Model

**Model:** Wan-AI/Wan2.1-I2V-14B-480P (Diffusers format, FP16)
**Source:** https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P
**Size:** ~30 GB (7 sharded safetensors files)

```bash
pip install huggingface-hub

# Create model directories
mkdir -p ~/ComfyUI/models/diffusion_models
mkdir -p ~/ComfyUI/models/text_encoders
mkdir -p ~/ComfyUI/models/clip_vision
mkdir -p ~/ComfyUI/models/vae

# Download the I2V-14B-480P model (Diffusers format)
huggingface-cli download Wan-AI/Wan2.1-I2V-14B-480P --local-dir ~/ComfyUI/models/diffusion_models/Wan2.1-I2V-14B-480P

# Download text encoder (T5)
huggingface-cli download Kijai/WanVideo_comfy umt5-xxl-enc-bf16.safetensors --local-dir ~/ComfyUI/models/text_encoders

# Download CLIP vision
huggingface-cli download Kijai/WanVideo_comfy open-clip-xlm-roberta-large-vit-huge-14_visual_fp16.safetensors --local-dir ~/ComfyUI/models/clip_vision

# Download VAE
huggingface-cli download Kijai/WanVideo_comfy Wan2_1_VAE_bf16.safetensors --local-dir ~/ComfyUI/models/vae
```

---

## Step 5: Start ComfyUI

### Option A: Direct web access (port 8188 open to your IP)

```bash
cd ~/ComfyUI
python main.py --listen 0.0.0.0 --port 8188
```
Then open `http://<INSTANCE_PUBLIC_IP>:8188`

### Option B: SSH tunneling (recommended — no open ports)

On your local machine:
```bash
ssh -i reels-factory-key.pem -L 8188:localhost:8188 ubuntu@<INSTANCE_PUBLIC_IP>
```
Then on the instance:
```bash
cd ~/ComfyUI
python main.py --listen 127.0.0.1 --port 8188
```
Then open `http://localhost:8188`

---

## Step 6: Load the I2V Workflow

**Exact workflow file:** `wanvideo_2_1_14B_I2V_example_03.json`

**Source:** https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_2_1_14B_I2V_example_03.json

**How to load:**
1. In ComfyUI, click **"Load"**
2. Navigate to: `~/ComfyUI/custom_nodes/ComfyUI-WanVideoWrapper/example_workflows/`
3. Select: `wanvideo_2_1_14B_I2V_example_03.json`

**If the file doesn't exist yet** (wrapper version may differ), download it directly:
```bash
wget -O ~/ComfyUI/custom_nodes/ComfyUI-WanVideoWrapper/example_workflows/wanvideo_2_1_14B_I2V_example_03.json https://raw.githubusercontent.com/kijai/ComfyUI-WanVideoWrapper/main/example_workflows/wanvideo_2_1_14B_I2V_example_03.json
```

---

## Step 7: Prepare the Input Image

1. Generate a start image using ChatGPT
2. Save as PNG, 480p resolution (854x480)
3. In ComfyUI, use **LoadImage** node to load it

---

## Step 8: Configure and Generate

The workflow should auto-configure. Key parameters to verify:

| Parameter | Expected Value |
|---|---|
| Model | Wan2.1-I2V-14B-480P |
| Width | 854 |
| Height | 480 |
| Frames | 81 (~3 sec at 24fps) |
| Steps | 40 |
| Seed | 42 (or any fixed number) |

Click **"Queue Prompt"** to generate.

**Generation time:** UNKNOWN — not yet validated on g5.xlarge. Expect several minutes.

---

## Step 9: Download the Output

```bash
# Via SCP from your local machine
scp -i reels-factory-key.pem ubuntu@<INSTANCE_PUBLIC_IP>:~/ComfyUI/output/*.mp4 .
```

---

## Step 10: Record Results

Fill in `COST_TRACKING_TEMPLATE.md` with actual measurements.

---

## Step 11: Clean Up — CRITICAL

### Terminate the instance:
```bash
aws ec2 terminate-instances --instance-ids i-xxxxxxxx --region us-east-2
```

### Verify cleanup:
1. **EC2 Instances:** https://console.aws.amazon.com/ec2/home?region=us-east-2#Instances:
2. **EBS Volumes:** https://console.aws.amazon.com/ec2/home?region=us-east-2#Volumes:
3. **Elastic IPs:** https://console.aws.amazon.com/ec2/home?region=us-east-2#Addresses:
4. **Snapshots:** https://console.aws.amazon.com/ec2/home?region=us-east-2#Snapshots:
5. **Security Groups:** https://console.aws.amazon.com/ec2/home?region=us-east-2#SecurityGroups:

---

## Troubleshooting

### CUDA out of memory
- Use FP8 model: `Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors` from Kijai/WanVideo_comfy
- Enable block swapping in the model loader node
- Reduce frames (try 41) or resolution (640x360)

### Model download too slow
- I2V-14B is ~30 GB — expect 10-30 minutes
- Use `screen` or `tmux` to keep download running

---

## Fallback: RunPod

If AWS is too cumbersome:
1. https://www.runpod.io → fund $10 minimum
2. Select GPU pod with 24+ GB VRAM (RTX 3090/4090, A5000)
3. Use Community Cloud template "ComfyUI"
4. Run the same workflow, terminate after test

---

## Direct Links

- EC2 Launch: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- Wan2.1-I2V-14B-480P: https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P
- I2V workflow: https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_2_1_14B_I2V_example_03.json
- Kijai models: https://huggingface.co/Kijai/WanVideo_comfy
- ComfyUI: https://github.com/comfyanonymous/ComfyUI
- WanVideoWrapper: https://github.com/kijai/ComfyUI-WanVideoWrapper
