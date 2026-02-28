#!/usr/bin/env python3
"""
Gökbörü Cyber Defense Node
Operates as a daemon inspecting all ROS2 / DDS traffic and hardware metrics.
Integrates the Scikit-Learn IsolationForest anomaly detector into an active defense mechanism.
"""

import time
import logging
import threading
import random
from anomaly_detector import GuardianAnomalyDetector

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [CYBER-DEFENSE] - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CyberDefenseNode:
    def __init__(self):
        logger.info("Initializing Cyber Defense Node...")
        self.detector = GuardianAnomalyDetector()
        self.is_active = False
        self.threat_level = "GREEN"

    def boot_sequence(self):
        logger.info("Running baseline calibration (Boot Sequence)...")
        self.detector.calibrate(num_samples=200)
        self.is_active = True
        logger.info("Defense Node Armed. Monitoring telemetry streams.")

    def monitor_stream(self):
        """Simulates continuous monitoring of vehicle streams."""
        while self.is_active:
            # Simulate real-time data pulling
            # [motor_temp, lidar_noise, voltage_drop, latency_ms]
            current_telemetry = [
                random.uniform(35.0, 42.0),
                random.uniform(0.1, 0.3),
                random.uniform(0.05, 0.1),
                random.uniform(5.0, 12.0)
            ]
            
            # Inject random anomaly for testing purposes (1% chance)
            if random.random() < 0.01:
                logger.warning("Simulating sudden voltage drop & latency spike (Potential Jamming/Hardware Failure)")
                current_telemetry[2] = 2.5 # Huge drop
                current_telemetry[3] = 300.0 # High latency

            is_anomaly, score = self.detector.analyze_telemetry(current_telemetry)
            
            if is_anomaly:
                self.threat_level = "RED"
                self.trigger_lockdown(score)
            else:
                self.threat_level = "GREEN"

            time.sleep(1) # Inspect 1Hz loop

    def trigger_lockdown(self, severity_score):
        logger.error(f"[!!!] ANOMALY DETECTED. SEVERITY: {severity_score:.2f}")
        logger.error("Executing Protocol: STOPPING MOTORS, ISOLATING NETWORK.")
        # Actual implementation would publish to /cmd_vel and drop DDS peers.
        time.sleep(2)
        logger.info("Lockdown complete. Manual override required.")
        self.is_active = False

if __name__ == "__main__":
    node = CyberDefenseNode()
    node.boot_sequence()
    
    # Run in a separate thread mimicking ROS nodes
    monitor_thread = threading.Thread(target=node.monitor_stream)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    try:
        while node.is_active:
            time.sleep(0.5)
    except KeyboardInterrupt:
        logger.info("Defense Node shutting down via manual interrupt.")
        node.is_active = False
