import cv2
from ultralytics import YOLO
import time
import json
import os
from azure.iot.device import IoTHubDeviceClient, Message

# =========================================================
# 1. FOLDER SETUP (EVIDENCE STORAGE)
# =========================================================
if not os.path.exists("good_boards"): os.makedirs("good_boards")
if not os.path.exists("defective_boards"): os.makedirs("defective_boards")

# =========================================================
# 2. SOLUTION DATABASE
# =========================================================
SOLUTIONS = {
    "missing_hole": "Check CNC Drill Bit & Program",
    "mouse_bite": "Check Breakout Tabs / Routing",
    "open_circuit": "Repair Track with Conductive Ink",
    "short": "Remove Excess Copper / Check Etching",
    "spur": "Clean Etching Bath",
    "spurious_copper": "Clean Board Surface",
    "solder_bridge": "Apply Flux & Reflow",
    "solder_ball": "Clean Residue / Check Temp Profile",
    "loose_wire": "Resolder Connection",
    "component_missing": "Check Pick & Place Machine",
    "cold_solder": "Re-heat Joint",
    "component_misalignment": "Adjust Placement"
}

def get_solution(defect_name):
    key = defect_name.lower().replace(" ", "_")
    return SOLUTIONS.get(key, "Manual Inspection Required")

# =========================================================
# 3. CLOUD CONFIGURATION
# =========================================================
CONN_STR = "HostName=pcb-camera-hub-01.azure-devices.net;DeviceId=pcb-laptop-camera-01;SharedAccessKey=+3Xrh1tZPHIKu9cwMY4cPB62Y77XE56goFBhc/iqFVs="

try:
    print("🔌 Connecting to Azure Cloud...")
    client = IoTHubDeviceClient.create_from_connection_string(CONN_STR)
    client.connect()
    print("✅ Azure Connected!")
except:
    print("❌ Cloud Connection Failed (Running Offline)")
    client = None

def process_batch(board_id, defects_list):
    """Sends report and returns filename suffix"""
    timestamp = time.time()
    
    # --- PASS SCENARIO ---
    if not defects_list:
        print(f"🟢 [BOARD #{board_id}] STATUS: PASS")
        if client:
            msg = Message(json.dumps({"id": board_id, "status": "PASS", "ts": timestamp}))
            msg.custom_properties["alert"] = "false"
            client.send_message(msg)
        return "PASS"

    # --- FAIL SCENARIO ---
    print(f"🔴 [BOARD #{board_id}] STATUS: FAIL ({len(defects_list)} Defects)")
    details = []
    for d in defects_list:
        act = get_solution(d)
        print(f"   -> Detected: {d.ljust(20)} | Action: {act}")
        details.append({"defect": d, "action": act})

    if client:
        payload = {
            "id": board_id,
            "status": "FAIL",
            "count": len(defects_list),
            "details": details,
            "ts": timestamp
        }
        msg = Message(json.dumps(payload))
        msg.custom_properties["alert"] = "true"
        client.send_message(msg)
        print("   (Cloud Report Sent)")
    
    return "FAIL"

# =========================================================
# 4. LOAD MODELS
# =========================================================
model_a_path = r"C:\Users\padma\OneDrive\Desktop\PCB_Project\pcb defect.pt"
model_b_path = r"C:\Users\padma\OneDrive\Desktop\PCB_Project\soldering_model.pt"

print("Loading Models...")
model_a = YOLO(model_a_path)
model_b = YOLO(model_b_path)

# =========================================================
# 5. MAIN LOOP (BATCH MODE)
# =========================================================
cap = cv2.VideoCapture(0)
board_counter = 1

print("\n--- INDUSTRIAL BATCH MODE READY ---")
print("1. Position PCB in Camera View.")
print("2. Press [SPACEBAR] to Trigger Inspection (Snap Photo).")
print("3. Press [Q] to Quit.")

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Show Live Feed (No Boxes yet)
    display_frame = frame.copy()
    cv2.putText(display_frame, f"NEXT BOARD: #{board_counter}", (10, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(display_frame, "PRESS [SPACE] TO SCAN", (10, 450), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    cv2.imshow("Industrial Station", display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == 32: # SPACEBAR Pressed
        print(f"\n📸 SNAPSHOT TAKEN! Processing Board #{board_counter}...")
        
        # Run Inference on the FROZEN frame
        results_a = model_a(frame, verbose=False)
        results_b = model_b(frame, verbose=False)
        
        annotated_img = frame.copy()
        all_defects = []

        # Collect and Draw
        for r, color in [(results_a, (255, 0, 0)), (results_b, (0, 0, 255))]:
            for box in r[0].boxes:
                cls_id = int(box.cls[0])
                name = r[0].names[cls_id]
                all_defects.append(name)
                
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(annotated_img, (x1, y1), (x2, y2), color, 2)
                cv2.putText(annotated_img, name, (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Report & Cloud
        status = process_batch(board_counter, all_defects)
        
        # Save Evidence
        if status == "PASS":
            filename = f"good_boards/Board_{board_counter}_PASS.jpg"
        else:
            filename = f"defective_boards/Board_{board_counter}_FAIL.jpg"
        
        cv2.imwrite(filename, annotated_img)
        print(f" Evidence Saved: {filename}")
        
        # Show Result Freeze for 2 seconds
        cv2.putText(annotated_img, f"RESULT: {status}", (10, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0) if status=="PASS" else (0, 0, 255), 3)
        cv2.imshow("Industrial Station", annotated_img)
        cv2.waitKey(2000) # Freeze for 2 seconds to show operator
        
        board_counter += 1
        print("--- Ready for Next Board ---\n")

cap.release()
cv2.destroyAllWindows()
if client: client.shutdown()
