# pcb-defect-detection-yolov11-iot

Dual-stage PCB defect detection (Fabrication + Assembly) using YOLOv11, ONNX, and Azure IoT Telemetry.

---

## Project Highlights: An Industry-Ready Smart Inspection System

This is not just an object detection model—it is a complete industrial automation solution designed to solve real manufacturing challenges with speed, precision, and scalability.

### 1. Solves a Core Industrial Problem

Traditional PCB inspection is slow, expensive, and often inaccurate.  
This system provides a software-defined, adaptable alternative that:

- Reduces reliance on costly AOI hardware  
- Increases throughput with real-time inference  
- Improves consistency by eliminating operator fatigue  
- Adapts instantly to new defect types without expensive retooling  

---

## System Architecture

![System Architecture](system_architecture.png)

---

## 2. Strategic Dual-Model Architecture

The inspection pipeline is intentionally decoupled into two specialized stages to address the fundamentally different requirements of PCB fabrication and PCB assembly.  
This avoids the accuracy trade-offs and instability that occur in monolithic single-model systems.

### 2.1 Model A — Fabrication Stage (High-Precision Configuration)

**Role:** Inspects raw bare boards immediately after the etching process  
**Key Metric:** 94.88% precision  

**Technical Objectives:**

- Minimize false positives  
- Prevent rejection of functional boards  
- Maximize material yield  

Precision is prioritized because fabrication defects are relatively sparse but critical; over-flagging good boards directly increases scrap cost and disrupts production.

---

### 2.2 Model B — Assembly Stage (High-Recall Configuration)

**Role:** Inspects component-mounted PCBs after reflow soldering  
**Key Metric:** 91.33% recall  

**Technical Objectives:**

- Minimize false negatives  
- Ensure no defective boards escape to customers  
- Maximize final product reliability  

Recall is prioritized because missing a solder or placement defect can cause field failures, returns, and warranty costs.

---

### 2.3 Why a Dual-Model Approach?

- Fabrication and assembly stages have different visual patterns, defect distributions, and business risk profiles.  
- A single model tuned for one stage will typically underperform on the other.  
- Using two specialized models allows independent optimization of decision thresholds:  
  - Model A is tuned for **strict precision**.  
  - Model B is tuned for **strict recall**.  
- This architecture mirrors real SMT production lines and makes the system closer to an industry-ready AOI replacement rather than an academic demo.

---

## 3. Full Edge-to-Cloud Integration (Digital Twin Architecture)

The system extends beyond local inference to establish a closed-loop data pipeline from edge devices to the cloud, enabling a production-line Digital Twin.

### 3.1 Edge Logic and Action Mapping

Inference outputs from the YOLOv11 models are processed via a deterministic control script:

- Raw class labels are mapped to specific maintenance or inspection instructions.  
- The system produces **operational recommendations**, not just bounding boxes.

**Example mapping logic:**

If class == "Missing Hole" → Output: "Check CNC Drill Bit"
If class == "Solder Bridge" → Output: "Apply Flux & Reflow"

text

### 3.2 Cloud Telemetry

- Inspection metadata (class ID, confidence score, timestamp, mapped action) is serialized into JSON.  
- Messages are pushed to Microsoft Azure IoT Hub over MQTT, creating a continuous telemetry stream suitable for dashboards, alerts, and analytics.

---

## 4. Engineered for the Factory Floor

This system is optimized for real-world deployment, not just offline benchmarks.

- **Throughput:** 78.5 FPS, compatible with high-speed conveyor lines.  
- **Deployment:** Models exported to ONNX for low-latency inference on edge devices such as NVIDIA Jetson and other lightweight industrial PCs.  

---

## Why This Matters

This project demonstrates a holistic engineering skillset combining:

- Deep Learning (YOLOv11, custom training)  
- Smart Instrumentation (camera-based inspection design)  
- Control Systems (feedback and corrective logic)  
- Industrial IoT (Azure, MQTT, real-time telemetry)  
- Edge Computing (ONNX optimization for deployment)  

The result is a practical, scalable, industry-grade inspection system ready for modern manufacturing environments.
