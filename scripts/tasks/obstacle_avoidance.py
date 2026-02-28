#!/usr/bin/env python3
"""
Gökbörü Obstacle Avoidance (VFH Logic)
Implements Vector Field Histogram logic for local obstacle avoidance.
Essential for navigating the dynamic obstacle track in Teknofest İKA.
"""

import math
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='[O-AVOIDANCE] %(message)s')

class VectorFieldHistogram:
    def __init__(self, num_sectors=72, max_range=5.0, safety_radius=0.7):
        """
        Divides the 360 view into sectors (e.g., 72 sectors of 5 degrees).
        Thresholds paths based on obstacle density.
        """
        self.num_sectors = num_sectors
        self.max_range = max_range
        self.safety_radius = safety_radius
        self.histogram = np.zeros(self.num_sectors)
        logging.info("VFH Obstacle Avoidance Module Initialized.")

    def update_histogram(self, lidar_ranges, min_angle, increment):
        """Constructs the polar histogram from laser scans."""
        self.histogram = np.zeros(self.num_sectors)
        
        for i, r in enumerate(lidar_ranges):
            if r < self.max_range and r > 0.1: # Valid reading
                # Calculate obstacle magnitude (closer = higher magnitude)
                magnitude = 1.0 - (r / self.max_range)**2
                
                # Determine sector
                angle = min_angle + (i * increment)
                sector_idx = int((angle + math.pi) / (2 * math.pi) * self.num_sectors) % self.num_sectors
                
                # Add to histogram (accounting for robot size)
                enlargement = math.asin(self.safety_radius / r) if self.safety_radius < r else math.pi/4
                spread = int(enlargement / (2 * math.pi / self.num_sectors))
                
                for offset in range(-spread, spread + 1):
                    idx = (sector_idx + offset) % self.num_sectors
                    self.histogram[idx] += magnitude

    def calculate_evasive_vector(self, target_heading):
        """Finds the lowest cost sector close to the target heading."""
        # Cost function: c1 * obstacle_density + c2 * deviation_from_target
        threshold = 2.0 # Sector considered blocked if magnitude above this
        
        best_sector = -1
        min_cost = float('inf')
        
        target_sector = int((target_heading + math.pi) / (2 * math.pi) * self.num_sectors) % self.num_sectors

        for i in range(self.num_sectors):
            if self.histogram[i] < threshold:
                # Caclulate deviation (handling circular wrapping)
                deviation = abs(target_sector - i)
                if deviation > self.num_sectors / 2:
                    deviation = self.num_sectors - deviation
                    
                cost = (self.histogram[i] * 5.0) + (deviation * 1.5)
                
                if cost < min_cost:
                    min_cost = cost
                    best_sector = i

        if best_sector == -1:
            logging.critical("ALL SECTORS BLOCKED! EMERGENCY HALT REQUIRED.")
            return None # Stop

        # Convert back to angle
        evasive_angle = (best_sector / self.num_sectors) * 2 * math.pi - math.pi
        return evasive_angle

if __name__ == "__main__":
    vfh = VectorFieldHistogram()
    
    # Simulate Lidar Scan with an obstacle straight ahead (0 rad)
    dummy_ranges = np.ones(360) * 4.0
    dummy_ranges[170:190] = 0.8 # Obstacle directly front
    
    vfh.update_histogram(dummy_ranges, -math.pi, math.pi/180)
    
    # Target is straight ahead, but blocked.
    evasive_angle = vfh.calculate_evasive_vector(target_heading=0.0)
    
    if evasive_angle is not None:
        print(f">> Threat ahead. Commencing evasive maneuver towards {math.degrees(evasive_angle):.1f} degrees.")
    else:
        print(">> No safe path found.")
