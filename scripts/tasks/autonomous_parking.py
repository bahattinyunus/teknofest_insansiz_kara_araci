#!/usr/bin/env python3
"""
Gökbörü Autonomous Parking Logic
Designed specifically for the Teknofest İnsansız Kara Aracı (İKA) competition.
Uses Lidar scan data to detect parking boundaries (cones/lines) and calculates
a geometric path for parallel or perpendicular parking.
"""

import math
import logging

logging.basicConfig(level=logging.INFO, format='[PARKING-AI] %(message)s')

class AutonomousParkingState:
    SCANNING = 0
    ALIGNING = 1
    REVERSING = 2
    ADJUSTING = 3
    PARKED = 4

class AutonomousParker:
    def __init__(self, vehicle_length=0.65, vehicle_width=0.45):
        self.state = AutonomousParkingState.SCANNING
        self.length = vehicle_length
        self.width = vehicle_width
        self.target_slot = None
        logging.info("Autonomous Parking Module Initialized.")

    def process_lidar_scan(self, ranges, min_angle, max_angle, increment):
        """
        Mock implementation of finding a parking slot using Lidar.
        In reality, we look for two distinct 'jumps' in distance indicating a gap.
        """
        if self.state != AutonomousParkingState.SCANNING:
            return

        logging.info(f"Scanning environment with {len(ranges)} Lidar rays...")
        
        # Simulated gap detection logic
        gap_found = True
        gap_width = 1.2 # Meters (Teknofest standard typically > vehicle + margin)
        
        if gap_found and gap_width > self.length * 1.5:
            logging.info(f"Target slot acquired. Width: {gap_width}m")
            self.target_slot = {"x": 2.0, "y": -1.0} # Target relative position
            self.state = AutonomousParkingState.ALIGNING

    def compute_parking_maneuver(self):
        """Generates velocity commands based on the current parking state."""
        lin = 0.0
        ang = 0.0
        
        if self.state == AutonomousParkingState.ALIGNING:
            logging.info("Aligning parallel to the parking slot...")
            # Simulate alignment taking place
            self.state = AutonomousParkingState.REVERSING
            lin = 0.5
            ang = 0.0
            
        elif self.state == AutonomousParkingState.REVERSING:
            logging.info("Executing reverse S-curve maneuver...")
            lin = -0.3
            ang = -0.5
            # Simulate maneuver completion
            self.state = AutonomousParkingState.ADJUSTING
            
        elif self.state == AutonomousParkingState.ADJUSTING:
            logging.info("Adjusting position within the bounding lines...")
            lin = 0.1
            ang = 0.5
            self.state = AutonomousParkingState.PARKED
            
        elif self.state == AutonomousParkingState.PARKED:
            logging.info("SUCCESS: Vehicle successfully parked within limits.")
            lin = 0.0
            ang = 0.0
            
        return lin, ang

if __name__ == "__main__":
    parker = AutonomousParker()
    
    # Simulate Lidar Scan
    dummy_ranges = [5.0] * 360
    parker.process_lidar_scan(dummy_ranges, -math.pi, math.pi, math.pi/180)
    
    # Simulate Control Loop
    while parker.state != AutonomousParkingState.PARKED:
        vel, ang = parker.compute_parking_maneuver()
        print(f">> Cmd: Lin {vel:.2f}, Ang {ang:.2f}")
    
    print(">> Parking Sequence Complete.")
