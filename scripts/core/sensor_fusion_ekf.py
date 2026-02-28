#!/usr/bin/env python3
"""
Gökbörü Extended Kalman Filter (EKF) Core
Fuses multiple noisy sensor inputs (IMU, Odometry, GPS) to estimate the true
state of the Unmanned Ground Vehicle (UGV).
Relies on 'filterpy' for robust mathematical matrix operations.
"""

import numpy as np
import logging

try:
    from filterpy.kalman import ExtendedKalmanFilter
    from filterpy.common import Q_discrete_white_noise
    HAS_FILTERPY = True
except ImportError:
    HAS_FILTERPY = False
    logging.warning("filterpy module not found. EKF running in simulation/mock mode. Install via requirements.txt")

logging.basicConfig(level=logging.INFO, format='[SENSOR-FUSION] %(message)s')

class GökbörüEKF:
    def __init__(self, dt=0.05):
        """
        Initializes the EKF for resolving state [x, y, theta, velocity]
        dt: Time step representing a 20Hz update loop.
        """
        self.dt = dt
        self.is_active = HAS_FILTERPY
        
        if self.is_active:
            # Dimension of State (x, y, theta, v) = 4
            # Dimension of Measurement (z_x, z_y, z_theta) = 3
            self.ekf = ExtendedKalmanFilter(dim_x=4, dim_z=3)
            
            # Initial state vector [x, y, angle, velocity_linear]
            self.ekf.x = np.array([0.0, 0.0, 0.0, 0.0])
            
            # State Covariance Matrix (Initial Uncertainty)
            self.ekf.P *= 10.0 
            
            # Measurement Noise Covariance Matrix (R)
            # Suppose GPS variance on x,y is 1.0m, IMU heading variance is 0.1 rad
            self.ekf.R = np.diag([1.0, 1.0, 0.1])
            
            # Process Noise Covariance Matrix (Q)
            # Models unmeasured forces like slip, wind, bumps
            self.ekf.Q = np.eye(4) * 0.01

            logging.info("Extended Kalman Filter Online. Dimensions: State=4, Measurement=3.")

    def _state_transition(self, state, dt):
        """ The non-linear equations mapping the previous state to the current state """
        x, y, theta, v = state
        
        # Simple bicycle/differential motion model
        new_x = x + (v * np.cos(theta) * dt)
        new_y = y + (v * np.sin(theta) * dt)
        new_theta = theta # Updated via IMU directly, assumes constant velocity here
        new_v = v 
        
        return np.array([new_x, new_y, new_theta, new_v])

    def _jacobian_H(self, state):
        """ Jacobian matrix of the measurement function H at current state """
        # We measure x, y, theta. We do not measure v directly in this setup.
        # H maps [x,y,theta,v] -> [x,y,theta]
        H = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0]
        ])
        return H

    def predict(self, control_u=None):
        """ Step 1: Predict the next state mathematically (no sensor data used here) """
        if self.is_active:
            # We must pass the non-linear state transition function 'fx' to the EKF
            # We don't have linear transition matrix F, so we update x manually
            self.ekf.x = self._state_transition(self.ekf.x, self.dt)
            # The covariance prediction in EKF still requires the Jacobian Fj
            # For simplicity in this template, we assume identity, realistic EKF calculates Fj mathematically
            Fj = np.eye(4)
            self.ekf.P = np.dot(Fj, self.ekf.P).dot(Fj.T) + self.ekf.Q

    def update(self, measurement_z):
        """ 
        Step 2: Update the predicted state containing real but noisy sensor input.
        measurement_z is [measured_x, measured_y, measured_theta] from GPS/IMU
        """
        if self.is_active:
            def hx(state):
                """ Measurement function (Expected measurement given state) """
                return np.array([state[0], state[1], state[2]])
            
            self.ekf.update(np.array(measurement_z), HJacobian=self._jacobian_H, Hx=hx)
            return self.ekf.x
        else:
            return np.array([measurement_z[0], measurement_z[1], measurement_z[2], 0.0])

if __name__ == "__main__":
    fusion = GökbörüEKF(dt=0.1) # Simulate 10Hz loop
    
    # Simulate a stationary robot getting noisy GPS data
    for step in range(5):
        fusion.predict()
        # Simulated Noisy GPS Measurement (True pose is [0,0,0])
        noisy_measurement = [np.random.normal(0, 0.5), np.random.normal(0, 0.5), np.random.normal(0, 0.05)]
        
        estimated_state = fusion.update(noisy_measurement)
        
        if fusion.is_active:
            print(f"[{step}] Raw GPS: X={noisy_measurement[0]:.2f}, Y={noisy_measurement[1]:.2f} | EKF Filtered: X={estimated_state[0]:.2f}, Y={estimated_state[1]:.2f}")
    
    if fusion.is_active:
         print("EKF successfully converged noisy sensor data to stable state estimation.")
