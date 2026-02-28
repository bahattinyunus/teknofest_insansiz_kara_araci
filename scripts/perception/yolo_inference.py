#!/usr/bin/env python3
"""
Gökbörü YOLOv8 Tactical Inference Engine
Highly optimized object detection for autonomous UGV operations.
Supports: Obstacle detection, Target identification, and Threat assessment.
"""

import cv2
import numpy as np
import time
from ultralytics import YOLO

class GökbörüYOLO:
    def __init__(self, model_path="yolov8n.pt"):
        print("[*] Loading Gökbörü Tactical Vision (YOLOv8)...")
        # In a real scenario, we'd use .engine for TensorRT on Jetson
        self.model = YOLO(model_path)
        self.classes = self.model.names
        print(f"[+] Model loaded with {len(self.classes)} identifiable targets.")

    def infer(self, frame):
        """Runs inference on a single frame and returns detections."""
        start_time = time.time()
        results = self.model(frame, stream=True, verbose=False)
        
        detections = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = box.conf[0]
                cls = int(box.cls[0])
                label = self.classes[cls]
                
                if conf > 0.5:
                    detections.append({
                        "label": label,
                        "confidence": float(conf),
                        "bbox": [int(x1), int(y1), int(x2), int(y2)]
                    })
        
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        return detections, fps

    def draw_detections(self, frame, detections):
        """Utility to visualize tactical insights on the frame."""
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            label = det["label"]
            conf = det["confidence"]
            
            # Dramatic UI color (Gökbörü Cyan)
            color = (255, 255, 0) # Cyan in BGR
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return frame

if __name__ == "__main__":
    # Test simulation
    print(">> RUNNING TACTICAL VISION TEST...")
    detector = GökbörüYOLO()
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    dets, fps = detector.infer(dummy_frame)
    print(f">> Inference successful. FPS: {fps:.2f} | Detections: {len(dets)}")
