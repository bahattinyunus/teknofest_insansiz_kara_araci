#!/usr/bin/env python3
"""
Gökbörü Pure Pursuit Controller
Calculates the target steering angle to follow a predefined path of waypoints.
Core algorithm for autonomous UGV navigation in URC/TEKNOFEST.
"""

import numpy as np

class PurePursuitController:
    def __init__(self, lookahead_distance=1.0, wheelbase=0.5):
        self.L = wheelbase
        self.ld = lookahead_distance

    def calculate_steering(self, current_pos, current_heading, path):
        """
        Calculates steering angle.
        current_pos: [x, y]
        path: List of [[x, y], ...]
        """
        # 1. Find the target point on the path
        target_pt = self._find_target_point(current_pos, path)
        
        # 2. Transform target point to robot's local frame
        dx = target_pt[0] - current_pos[0]
        dy = target_pt[1] - current_pos[1]
        
        # Local transformation
        alpha = np.arctan2(dy, dx) - current_heading
        
        # 3. Calculate steering angle delta
        # delta = atan2(2 * L * sin(alpha) / ld)
        steering_angle = np.arctan2(2 * self.L * np.sin(alpha), self.ld)
        
        return steering_angle

    def _find_target_point(self, pos, path):
        # Simplistic approach: find point closest to lookahead distance
        # In real robots, we use line-circle intersection.
        distances = [np.linalg.norm(np.array(pt) - np.array(pos)) for pt in path]
        closest_idx = np.argmin(np.abs(np.array(distances) - self.ld))
        return path[closest_idx]

if __name__ == "__main__":
    controller = PurePursuitController()
    path = [[0, 0], [1, 0], [2, 1], [3, 2], [5, 2]]
    angle = controller.calculate_steering([0, 0], 0, path)
    print(f">> Calculated Steering Angle: {np.degrees(angle):.2f} degrees")
