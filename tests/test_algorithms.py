import pytest
import numpy as np
import sys
import os

# Ensure project scripts are in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.control.pure_pursuit import PurePursuitController
from scripts.perception.sign_detection import SignDetector

def test_pure_pursuit_straight_line():
    """Verify that steering is zero for a straight path ahead."""
    controller = PurePursuitController(lookahead_distance=1.0, wheelbase=0.5)
    path = [[0, 0], [1, 0], [2, 0]]
    current_pos = [0, 0]
    current_heading = 0 # Radians
    
    steering = controller.calculate_steering(current_pos, current_heading, path)
    assert np.isclose(steering, 0.0, atol=0.1)

def test_pure_pursuit_left_turn():
    """Verify that steering is positive (left) for a left turn."""
    controller = PurePursuitController(lookahead_distance=1.0, wheelbase=0.5)
    path = [[0, 0], [0, 1], [0, 2]]
    current_pos = [0, 0]
    current_heading = 0
    
    steering = controller.calculate_steering(current_pos, current_heading, path)
    assert steering > 0

def test_sign_detector_logic():
    """Verify that sign detector handles empty frames."""
    detector = SignDetector()
    dummy_frame = np.zeros((100, 100, 3), dtype=np.uint8)
    results, _, _ = detector.detect(dummy_frame)
    
    assert results["red_detected"] == False
    assert results["blue_detected"] == False
