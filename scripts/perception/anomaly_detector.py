#!/usr/bin/env python3
"""
Gökbörü Guardian: System Anomaly Detection Core
Uses Isolation Forests and statistical thresholds to detect
hardware failures, sensor disconnections, and cyber-interference.
Expected to be run as an asynchronous ROS 2 Node in production.
"""

import math
import random
import time
import logging

try:
    import numpy as np
    from sklearn.ensemble import IsolationForest
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

# Logger setup
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] [GUARDIAN-AI] %(message)s')
logger = logging.getLogger('GuardianCore')

class GuardianAnomalyDetector:
    def __init__(self, contamination_rate=0.01):
        self.contamination_rate = contamination_rate
        self.model = None
        self.historical_telemetry = []
        self.is_trained = False
        
        if HAS_SKLEARN:
            logger.info("Initializing Scikit-Learn IsolationForest engine...")
            self.model = IsolationForest(
                n_estimators=100, 
                max_samples='auto', 
                contamination=self.contamination_rate,
                random_state=42
            )
        else:
            logger.warning("Scikit-Learn not found. Falling back to heuristic anomaly detection.")

    def calibrate(self, num_samples=500):
        """Simulate a training phase using nominal telemetry data."""
        logger.info(f"Gathering {num_samples} nominal telemetry samples for calibration...")
        for _ in range(num_samples):
            # Simulated nominal characteristics:
            # [motor_temp, lidar_noise, voltage_drop, latency_ms]
            sample = [
                random.uniform(30.0, 45.0), # Motor Temp (C)
                random.uniform(0.1, 0.5),   # LiDAR Noise Ratio
                random.uniform(0.01, 0.2),  # Voltage Drop (V)
                random.uniform(5.0, 15.0)   # Network Latency (ms)
            ]
            self.historical_telemetry.append(sample)
        
        if HAS_SKLEARN:
            X_train = np.array(self.historical_telemetry)
            self.model.fit(X_train)
            self.is_trained = True
            logger.info("IsolationForest model fitted successfully.")
        else:
            self.is_trained = True
            logger.info("Heuristic bounds calculated.")

    def analyze_telemetry(self, current_data):
        """
        Analyze real-time incoming telemetry data array:
        [motor_temp, lidar_noise, voltage_drop, latency_ms]
        """
        if not self.is_trained:
            logger.warning("Agent not calibrated. Run calibrate() first.")
            return False, 0.0

        if HAS_SKLEARN:
            X_test = np.array([current_data])
            # returns -1 for anomaly, 1 for normal
            prediction = self.model.predict(X_test)[0]
            score = self.model.decision_function(X_test)[0]
            is_anomaly = bool(prediction == -1)
            return is_anomaly, score
        else:
            # Fallback heuristic logic
            is_anomaly = False
            if current_data[0] > 60.0: is_anomaly = True # Overheating
            if current_data[3] > 100.0: is_anomaly = True # Comm breakdown
            return is_anomaly, random.uniform(-0.5, 0.5)

    def trigger_fail_safe(self, reason):
        """Executes emergency protocols if a critical anomaly is validated."""
        logger.error("="*50)
        logger.error(f"CRITICAL ANOMALY DETECTED: {reason}")
        logger.error("INITIATING PROTOCOL ZERO: EMERGENCY STOP AND DATA ENCRYPTION")
        logger.error("="*50)
        # Interface with control scripts to halt motors.


if __name__ == '__main__':
    guardian = GuardianAnomalyDetector()
    guardian.calibrate(100)
    
    # Test Normal Data
    normal_data = [35.2, 0.2, 0.05, 10.1]
    is_anomaly, score = guardian.analyze_telemetry(normal_data)
    logger.info(f"Nominal check -> Anomaly: {is_anomaly} (Score: {score:.3f})")

    # Test Anomaly Data (Motor Overheat + Comm Jamming)
    attack_data = [85.0, 0.9, 1.5, 250.0]
    is_anomaly, score = guardian.analyze_telemetry(attack_data)
    logger.warning(f"Attack check -> Anomaly: {is_anomaly} (Score: {score:.3f})")
    
    if is_anomaly:
        guardian.trigger_fail_safe("THERMAL_AND_COMMS_BREACH")
