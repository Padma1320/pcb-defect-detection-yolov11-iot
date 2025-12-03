# pcb-defect-detection-yolov11-iot
Dual-stage PCB defect detection (Fabrication + Assembly) using YOLOv11, ONNX, and Azure IoT Telemetry.
Project Highlights: An Industry-Ready Smart Inspection System

This is not just an object detection model—it is a complete industrial automation solution designed to solve real manufacturing challenges with speed, precision, and scalability.

1. Solves a Core Industrial Problem

Traditional PCB inspection is slow, expensive, and often inaccurate.
This system provides a software-defined, adaptable alternative that:

Reduces reliance on costly AOI hardware

Increases throughput with real-time inference

Improves consistency by eliminating operator fatigue

Adapts instantly to new defect types without expensive retooling

2. Strategic Dual-Model Architecture

Instead of forcing every defect through a single model, the inspection pipeline mirrors an actual SMT production line.

Model A (Fabrication) — The Yield Guardian

Inspects raw bare boards immediately after etching

Precision: 94.88%

Prevents unnecessary scrapping of good boards, reducing raw material loss

Model B (Assembly) — The Risk Mitigator

Inspects populated boards after reflow

Recall: 91.33%

Ensures no defect escapes reach the customer, protecting brand reputation

This dual-stream architecture provides significantly higher reliability than a monolithic single-model system.

3. Full Edge-to-Cloud Integration (Digital Twin Architecture)

The project goes beyond visual detection and builds a complete smart manufacturing data loop.

Edge Intelligence (Action Mapping)

Each detection is converted into a corrective instruction.
Example:
“Missing Hole” → “Inspect CNC Drill Bit”

Cloud Telemetry (Digital Twin)

All inspection data is serialized into JSON and pushed to Microsoft Azure IoT Hub via MQTT.
This enables:

Predictive maintenance

Historical quality tracking

Remote factory monitoring

4. Engineered for the Factory Floor

This system is designed for deployment—not just academic performance.

High Throughput: 78.5 FPS, compatible with high-speed conveyor lines

Edge-Ready: ONNX-exported models enable low-latency inference on devices such as NVIDIA Jetson

Why This Matters

This project demonstrates a holistic engineering skillset combining:

Deep Learning (YOLOv11, custom training)

Smart Instrumentation (sensor-based inspection design)

Control Systems (feedback and corrective logic)

Industrial IoT (Azure, MQTT, telemetry pipelines)

Edge Computing (ONNX optimization for deployment)

The result is a practical, scalable, industry-grade inspection system ready for modern manufacturing environments.
