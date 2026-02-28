#!/usr/bin/env python3
"""
Gökbörü Tactical Sign Detection
Color-based segmentation for red (STOP/NO ENTRY) and blue (DIRECTION) signs.
Essential for Teknofest İKA traffic rule compliance tasks.
"""

import cv2
import numpy as np

class SignDetector:
    def __init__(self):
        # HSV Color Thresholds (Approximate)
        self.red_lower1 = np.array([0, 100, 100])
        self.red_upper1 = np.array([10, 255, 255])
        self.red_lower2 = np.array([160, 100, 100])
        self.red_upper2 = np.array([180, 255, 255])
        
        self.blue_lower = np.array([100, 150, 0])
        self.blue_upper = np.array([140, 255, 255])

    def detect(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Red Mask (two ranges for wrap-around)
        mask_red1 = cv2.inRange(hsv, self.red_lower1, self.red_upper1)
        mask_red2 = cv2.inRange(hsv, self.red_lower2, self.red_upper2)
        mask_red = cv2.add(mask_red1, mask_red2)
        
        # Blue Mask
        mask_blue = cv2.inRange(hsv, self.blue_lower, self.blue_upper)
        
        results = {
            "red_detected": cv2.countNonZero(mask_red) > 1000,
            "blue_detected": cv2.countNonZero(mask_blue) > 1000
        }
        return results, mask_red, mask_blue

if __name__ == "__main__":
    detector = SignDetector()
    cap = cv2.VideoCapture(0) # Open default camera for testing
    print(">> Press 'q' to exit Tactical sign calibration...")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        analysis, m_red, m_blue = detector.detect(frame)
        if analysis["red_detected"]:
            cv2.putText(frame, "!!! STOP SIGN DETECTED !!!", (50, 50), 
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
            
        cv2.imshow("Tactical View", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
