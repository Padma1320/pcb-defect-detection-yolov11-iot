## Project Highlights: An Industry-Ready Smart Inspection System

This is not just an object detection model—it is a complete industrial automation solution designed to solve real manufacturing challenges with speed, precision, and scalability.

---
### 1. Solves a Core Industrial Problem

Traditional PCB inspection is slow, expensive, and often inaccurate.  
This system provides a software-defined, adaptable alternative that:

- Reduces reliance on costly AOI hardware  
- Increases throughput with real-time inference  
- Improves consistency by eliminating operator fatigue  
- Adapts instantly to new defect types without expensive retooling  

---
### 2. Strategic Dual-Model Architecture

Instead of forcing every defect through a single model, the inspection pipeline mirrors an actual SMT production line.
#### **Model A (Fabrication) — The Yield Guardian**

- Inspects raw bare boards immediately after etching  
- Precision: **94.88%**  
- Prevents unnecessary scrapping of good boards, reducing material loss  

#### **Model B (Assembly) — The Risk Mitigator**

- Inspects populated boards after reflow soldering  
- Recall: **91.33%**  
- Ensures zero "defect escapes" reach the customer  

This dual-stream approach significantly improves reliability over monolithic single-model systems.

---
### 3. Full Edge-to-Cloud Integration (Digital Twin Architecture)

This project extends beyond visual detection to build a complete smart manufacturing data loop.
#### **Edge Intelligence (Action Mapping)**

Every detection triggers a specific business rule.

## System Architecture

![System Architecture](system_architecture.png)


Example:  
- Defect: *Missing Hole*  
- Action: *Inspect CNC Drill Bit*
#### **Cloud Telemetry (Azure IoT Hub)**

Inspection data is serialized into JSON and pushed via MQTT, enabling:

- Predictive maintenance  
- Historical quality tracking  
- Remote factory monitoring  

---
### 4. Engineered for the Factory Floor

This system is optimized for real-world deployment:

- **78.5 FPS** throughput for high-speed conveyor environments  
- ONNX-exported models for low-latency edge inference  
- Works on Jetson devices, Raspberry Pi, and lightweight edge hardware  

---
### Why This Matters

This project demonstrates a holistic engineering skillset combining:

- Deep Learning (YOLOv11, Custom Training)  
- Smart Instrumentation (Sensor Integration)  
- Control Systems (Feedback Logic)  
- Industrial IoT (Azure, MQTT, Telemetry)  
- Edge Computing (ONNX Optimization)  

The result is a practical, scalable, and industry-grade inspection system ready for modern manufacturing environments.
