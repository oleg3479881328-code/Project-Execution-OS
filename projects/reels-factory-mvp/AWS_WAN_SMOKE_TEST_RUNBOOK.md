# AWS Wan Smoke Test Runbook — Reels Factory MVP

Date: 2026-06-10
Target: One 3-second 480p Wan Image-to-Video generation on AWS g4dn.xlarge
Author: Infrastructure executor

---

## Before You Start

- You have AWS credits: **$74.57** (expires 2026-10-04)
- GPU quota is approved: **4 vCPU** (g4dn.xlarge fits exactly)
- Region: **us-east-2** (Ohio)
- Budget for this test: **~$1-2** (1-2 hours of runtime)
- **Do not leave the instance running after the test.**

---

## Step 1: Launch the EC2 Instance

### Via AWS Console (recommended for first time)

1. Open EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
2. Click **Launch instance**
3. Name: `reels-factory-smoke-test`
4. **AMI:** Select **Deep Learning AMI GPU PyTorch 2.x (Ubuntu 22.04)** — this comes with CUDA, PyTorch, and NVIDIA drivers pre-installed
   - Search for "Deep Learning AMI GPU" in the AMI catalog
   - Select the latest Ubuntu 22.04 version
5. **Instance type:** `g4dn.xlarge` (4 vCPU, 16 GB VRAM)
6. **Key pair:** Select an existing key pair or create a new one
   - If creating: "Create new key pair" → name it `reels-factory-key` → download the `.pem` file
7. **Network settings:**
   - VPC: default
   - Subnet: any
   - **Security group:** Create new
     - Allow **SSH (22/TCP)** from your IP only (or 0.0.0.0/0 if you need access from anywhere)
     - Allow **HTTP (80/TCP)** from 0.0.0.0/0 (for ComfyUI web interface)
     - Allow **HTTPS (443/TCP)** from 0.0.0.0/0 (for ComfyUI web interface)
     - Allow **Custom TCP (8188)** from 0.0.0.0/0 (ComfyUI default port)
8. **Storage:** 30 GB gp3 root volume (default is fine)
9. **Advanced details:** Leave defaults
10. **Summary:** Review and click **Launch instance**

### Via AWS CLI (if you prefer)

```bash
# Create security group
aws ec2 create-security-group --group-name reels-factory-smoke-sg --description "Reels Factory smoke test SG" --region us-east-2

# Add SSH, HTTP, ComfyUI port rules
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 22 --cidr 0.0.0.0/0 --region us-east-2
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 80 --cidr 0.0.0.0/0 --region us-east-2
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 443 --cidr 0.0.0.0/0 --region us-east-2
aws ec2 authorize-security-group-ingress --group-name reels-factory-smoke-sg --protocol tcp --port 8188 --cidr 0.0.0.0/0 --region us-east-2

# Find the latest Deep Learning AMI GPU PyTorch 2.x
aws ec2 describe-images --region us-east-2 --owners amazon --filters "Name=name,Values=*Deep Learning AMI GPU PyTorch*" --query "Images[*].[ImageId,Name,CreationDate]" --output table

# Launch instance (replace ami-xxx with the actual AMI ID)
aws ec2 run-instances --image-id ami-xxx --instance-type g4dn.xlarge --key-name reels-factory-key --security-groups reels-factory-smoke-sg --block-device-mappings "[{\"DeviceName\":\"/dev/sda1\",\"Ebs\":{\"VolumeSize\":30,\"VolumeType\":\"gp3\"}}]" --region us-east-2
```

### ⏱ Expected setup time: 5 minutes

---

## Step 2: Connect to the Instance

```bash
# Make your key file readable only by you
chmod 400 reels-factory-key.pem

# SSH into the instance (replace with your instance's public IP)
ssh -i reels-factory-key.pem ubuntu@<INSTANCE_PUBLIC_IP>
```

**Where to find the public IP:**
- EC2 Console → Instances → select your instance → copy **Public IPv4 address**

### ⏱ Expected time: 1 minute

---

## Step 3: Install ComfyUI

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

# Install Wan2.1 wrapper for ComfyUI
cd custom_nodes
git clone https://github.com/kijai/ComfyUI-WanVideoWrapper.git
cd ..
```

### ⏱ Expected time: 5-10 minutes

---

## Step 4: Download the Wan I2V Model

Choose the smallest model for the first smoke test:

**Option A: Wan I2V 1.3B (recommended for first test)**
- VRAM: ~6-8 GB
- Quality: lower but sufficient for smoke test
- Download: ~3 GB

```bash
cd ~/ComfyUI/models/checkpoints

# Download Wan I2V 1.3B model
wget https://huggingface.co/Wan-AI/Wan2.1-I2V-1.3B/resolve/main/Wan2.1-I2V-1.3B.pth
```

**Option B: Wan I2V 14B (better quality, more VRAM)**
- VRAM: ~18-20 GB (fits in g4dn.xlarge with FP16)
- Download: ~30 GB

```bash
cd ~/ComfyUI/models/checkpoints

# Download Wan I2V 14B model (requires huggingface-cli login)
pip install huggingface-hub
huggingface-cli download Wan-AI/Wan2.1-I2V-14B --local-dir ./Wan2.1-I2V-14B
```

**For the first smoke test, use Option A (1.3B).**

### ⏱ Expected download time: 5-15 minutes (depends on model size)

---

## Step 5: Start ComfyUI

```bash
cd ~/ComfyUI
python main.py --listen 0.0.0.0 --port 8188
```

You should see output like:
```
Starting server
To see the GUI go to: http://0.0.0.0:8188
```

### ⏱ Expected time: 30 seconds

---

## Step 6: Access ComfyUI Web Interface

1. Open your browser
2. Go to: `http://<INSTANCE_PUBLIC_IP>:8188`
3. You should see the ComfyUI interface

**Troubleshooting:**
- If the page doesn't load, check that port 8188 is open in the security group
- Check that the instance has a public IP
- Try `curl -v http://localhost:8188` from the instance to verify ComfyUI is running

---

## Step 7: Load the Wan I2V Workflow

1. In ComfyUI, click **"Load"** (or drag and drop)
2. Load the Wan I2V workflow JSON file

**If you don't have a workflow file yet, create one:**

The minimal Wan I2V workflow needs these nodes:
- **LoadImage** — your input start image
- **LoadCheckpoint** — the Wan I2V model
- **WanVideoToVideo** (from ComfyUI-WanVideoWrapper) — the I2V generation node
- **VAEDecode** — decode the latent to video
- **VideoCombine** — combine frames into a video file
- **PreviewVideo** — preview in browser

**Simpler alternative:** Use the built-in example workflow from ComfyUI-WanVideoWrapper:
```bash
# Copy example workflow
cp ~/ComfyUI/custom_nodes/ComfyUI-WanVideoWrapper/example_workflows/wan_i2v.json ~/ComfyUI/
```
Then load `wan_i2v.json` in ComfyUI.

---

## Step 8: Prepare the Input Image

1. Generate a start image using ChatGPT (as decided in the project plan)
2. Save it as a PNG file
3. In ComfyUI, use the **LoadImage** node to load your image
4. Connect it to the WanVideoToVideo node

**Image requirements:**
- Resolution: 480p (854x480 or similar)
- Format: PNG
- Content: Simple scene (e.g., a car on a road)

---

## Step 9: Configure Generation Settings

In the WanVideoToVideo node, set:

| Parameter | Value |
|---|---|
| Model | Wan2.1-I2V-1.3B |
| Width | 854 |
| Height | 480 |
| Length | 81 frames (~3 seconds at 24fps) |
| Guidance Scale | 5.0 |
| Steps | 20 |
| Seed | 42 (or any fixed number for reproducibility) |

---

## Step 10: Generate!

1. Click **"Queue Prompt"** in ComfyUI
2. Wait for the generation to complete
3. The output video will appear in the **PreviewVideo** node

### ⏱ Expected generation time: 2-5 minutes

---

## Step 11: Download the Output

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

## Step 12: Record Results

Fill in the COST_TRACKING_TEMPLATE.md with your actual measurements.

---

## Step 13: Clean Up — CRITICAL

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
5. **Security Groups:** Delete the temporary security group (sg-reels-factory-smoke-sg)
   - https://console.aws.amazon.com/ec2/home?region=us-east-2#SecurityGroups:

### ⏱ Expected cleanup time: 2 minutes

---

## Troubleshooting

### "CUDA out of memory"
- Use the 1.3B model instead of 14B
- Reduce frame count (try 41 frames instead of 81)
- Reduce resolution (try 640x360)
- Enable memory optimizations in ComfyUI (`--lowvram` flag)

### "Cannot connect to ComfyUI"
- Check security group rules (port 8188 must be open)
- Check that ComfyUI is running (`ps aux | grep python`)
- Check the instance's public IP hasn't changed

### "Model download is too slow"
- Use `screen` or `tmux` to keep the download running in the background
- Consider using a smaller model variant

### "SSH connection refused"
- Wait 2-3 minutes after launching the instance (it takes time to boot)
- Check security group (port 22 must be open)
- Check that you're using the correct username (`ubuntu` for Ubuntu AMIs)

---

## Fallback Route: RunPod

If AWS setup becomes too cumbersome:

1. Go to https://www.runpod.io
2. Fund minimum **$10** (custom amount)
3. Select a GPU pod with similar specs (RTX 3090 or A5000, ~24 GB VRAM)
4. Use the Community Cloud template "ComfyUI" (pre-installed)
5. Upload your image and run the same Wan workflow
6. Terminate the pod after the test

---

## Direct Links

- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
- Launch Instance: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- ComfyUI: https://github.com/comfyanonymous/ComfyUI
- ComfyUI-WanVideoWrapper: https://github.com/kijai/ComfyUI-WanVideoWrapper
- Wan2.1 GitHub: https://github.com/Wan-Video/Wan2.1
- Wan2.1 I2V 1.3B (HuggingFace): https://huggingface.co/Wan-AI/Wan2.1-I2V-1.3B
- Wan2.1 I2V 14B (HuggingFace): https://huggingface.co/Wan-AI/Wan2.1-I2V-14B
