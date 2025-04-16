# 🔮 ComfyUI-MediaPipe-Vision

<div align="center">
  <h3>Google MediaPipe Vision AI for ComfyUI</h3>
  <p>A centralized implementation of MediaPipe vision tasks, optimized for real-time use</p>
</div>

---

## ✨ Overview

This repository provides a complete implementation of Google MediaPipe vision tasks for ComfyUI. It enables computer vision capabilities that can be used for interactive AI art, responsive interfaces, motion tracking, and advanced masking workflows.

## 🚀 Features

| Category | Available Tools |
|----------|-------------|
| **Face Analysis** | Face detection, face mesh (478 points), blendshapes, head pose |
| **Body Tracking** | Pose estimation (33 landmarks), segmentation masks |
| **Hand Analysis** | Hand tracking (21 landmarks per hand), gesture recognition |
| **Image Processing** | Object detection, image segmentation, image embeddings |
| **Creative Tools** | Face stylization, interactive segmentation |

## 📋 Supported MediaPipe Tasks

* **Face Detection:** Face bounding boxes and keypoints
* **Face Landmark Detection:** Face mesh landmarks with expression analysis
* **Hand Landmark Detection:** Hand position tracking with 21 landmarks
* **Pose Landmark Detection:** Body pose tracking with 33 landmarks
* **Object Detection:** Common object detection using models like EfficientDet
* **Image Segmentation:** Category-based image segmentation
* **Gesture Recognition:** Recognition of common hand gestures
* **Image Embedding:** Feature vector generation for image similarity
* **Interactive Segmentation:** User-guided image masking
* **Face Stylization:** Artistic style application to faces
* **Holistic Landmark Detection:** Full-body landmark detection (legacy)

> **Note:** Holistic landmark detection uses the legacy MediaPipe API as we await the official Tasks API release.

## 🧩 Project Structure

The extension is organized into these main components:

1. **Core MediaPipe Tasks** - Task implementations in `src/` directory for each vision capability
2. **ComfyUI Node Wrappers** - UI nodes in `node_wrappers/` organized by task type
3. **Processing Pipeline**:
   - **Model Loaders** - Prepare and configure MediaPipe models
   - **Detector Nodes** - Process images and extract vision data
   - **Position Extractors** - Get coordinates for specific landmarks
   - **Utility Nodes** - Create masks, calculate distances, control parameters

## ⚙️ Landmark System

The project's landmark system allows extracting and using position data:

### Position Extraction

**Landmark Position Extractors** access coordinate data from any landmark:
- Extract x, y, z positions from face, hand, or pose landmarks
- Access visibility and presence information where available
- Access world coordinates when available (hand and pose)
- Input landmark indices directly to access any point
- Process batches for multi-frame workflows

### Position Processing

Several node types work with landmark position data:

- **Delta Controls** - Track movement and map changes to parameter values
- **Proximity Nodes** - Calculate distances between landmarks
- **Masking Nodes** - Generate masks centered at landmark positions
- **Head Pose Extraction** - Calculate yaw, pitch, roll from face landmarks
- **Blendshape Analysis** - Extract facial expression parameters

### Example Workflow

```
Load Face Landmarker → Face Landmarker ← Image Input
           |
           ↓ landmarks
Face Landmark Position (Index: 1) → x,y,z coordinates
           |
           ↓ x,y,z
Position Delta Float Control → value → ComfyUI Parameter
```

## 🛠️ Installation

Use the ComfyUI-Manager, or:

```bash
# Navigate to your ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/your-username/ComfyUI-MediaPipe-Vision.git

# Enter the directory
cd ComfyUI-MediaPipe-Vision

# Install dependencies
pip install -r requirements.txt

# Restart ComfyUI
```

> **Note:** GPU Support varies by platform. For Linux, see [these instructions](https://ai.google.dev/edge/mediapipe/framework/getting_started/gpu_support).

## 🤝 Contributing

Contributions are welcome! Please open issues for bugs or feature requests.

This project provides flexible infrastructure for computer vision in ComfyUI. If you have ideas for:

- Creative AI interactions using vision
- Specific landmark tracking or detection needs
- Real-time vision workflows
- Improvements to the current implementation

Please open an issue, even if you're not sure how to implement it.

## 🔗 Related Projects

### [comfystream](https://github.com/yondonfu/comfystream)
A real-time streaming framework for ComfyUI that enables running workflows continuously on video streams, perfect for combining with MediaPipe vision capabilities.

### [ComfyUI_RealtimeNodes](https://github.com/ryanontheinside/ComfyUI_RealtimeNodes)
A suite of nodes for real-time ComfyUI workflows. Features include value animation, motion detection and tracking, sequence control, and more. Perfect companion for vision-based interactions.

### [ComfyUI-Stream-Pack](https://github.com/livepeer/ComfyUI-Stream-Pack)
A collection of ComfyUI nodes for multimedia streaming applications. Combines video processing with generative models for real-time media effects.

## 📜 License

[MIT License](LICENSE)



