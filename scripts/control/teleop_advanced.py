#!/usr/bin/env python3
"""
Gökbörü Advanced Teleop Controller
Provides safe manual override capabilities with Dead Man's Switch logic and Velocity Bounding.
Crucial for physical testing in ERC/Teknofest environments without compromising safety.
"""

import sys
import time
import logging

logging.basicConfig(level=logging.INFO, format='[TELEOP] %(message)s')

class AdvancedTeleop:
    def __init__(self):
        self.max_linear_vel = 2.0  # m/s
        self.max_angular_vel = 1.0 # rad/s
        self.current_linear = 0.0
        self.current_angular = 0.0
        self.dead_mans_switch_engaged = False

    def bound_velocity(self, lin, ang):
        lin = max(min(lin, self.max_linear_vel), -self.max_linear_vel)
        ang = max(min(ang, self.max_angular_vel), -self.max_angular_vel)
        return lin, ang

    def update_command(self, lin_input, ang_input, dms_pressed):
        """Updates internal state based on joypad/keyboard input."""
        if not dms_pressed:
            if self.dead_mans_switch_engaged:
                logging.warning("DEAD MAN'S SWITCH RELEASED! EMERGENCY BRAKING.")
            self.current_linear = 0.0
            self.current_angular = 0.0
            self.dead_mans_switch_engaged = False
            return

        self.dead_mans_switch_engaged = True
        self.current_linear, self.current_angular = self.bound_velocity(lin_input, ang_input)
        logging.info(f"Cmd Vel -> Linear: {self.current_linear:.2f} m/s | Angular: {self.current_angular:.2f} rad/s")

    def publish_cmd_vel(self):
        """Mock ROS publisher."""
        # publish(Twist(linear=self.current_linear, angular=self.current_angular))
        pass

if __name__ == "__main__":
    teleop = AdvancedTeleop()
    logging.info("Advanced Teleop Online. Awaiting inputs...")
    
    # Simulate an operations sequence
    teleop.update_command(1.5, 0.2, dms_pressed=True)
    teleop.publish_cmd_vel()
    time.sleep(1)
    
    # Try speeding over max (Should bound to 2.0)
    teleop.update_command(5.0, 0.0, dms_pressed=True) 
    teleop.publish_cmd_vel()
    time.sleep(1)
    
    # Release DMS (Emergency stop)
    teleop.update_command(5.0, 0.0, dms_pressed=False)
    teleop.publish_cmd_vel()
