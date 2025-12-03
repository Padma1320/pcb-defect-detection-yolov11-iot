# Model Weights (Download Links)

GitHub cannot host large .pt or .onnx files, so all trained PCB defect detection models
are stored in Google Drive.

Download or view all model files (Model A + Model B, PT + ONNX):
https://drive.google.com/drive/folders/1QKZGEH13oNbXKudQZXtfbP0hlwU1AqZY?usp=sharing

---

## Contents of the Drive Folder:
- model a.pt        (Model A - Fabrication, PyTorch format)
- model a.onnx      (Model A - Fabrication, ONNX export)
- model b.pt        (Model B - Assembly, PyTorch format)
- model b.onnx      (Model B - Assembly, ONNX export)

### Why ONNX Conversion?
The PyTorch (.pt) models were exported to ONNX to enable:
- Cross-platform inference (Python, C++, JavaScript, etc.)
- Faster runtime using ONNX Runtime on edge devices
- Easier deployment in industrial systems
- Compatibility with Intel OpenVINO and NVIDIA TensorRT

The ONNX models are functionally equivalent to the original PyTorch models, 
optimized for portable deployment.

