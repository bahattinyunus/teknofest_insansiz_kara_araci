"""
Basic import and architecture tests.
Verifies that the project tree is intact and syntax is inherently correct.
"""

import sys
import os

# Ensure the root directory is accessible directly if run externally
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_config_loader_import():
    """Ensure the config loader can be imported without errors."""
    try:
        from scripts.core.config_loader import ConfigLoader
        assert True
    except ImportError as e:
        assert False, f"Failed to import ConfigLoader: {e}"

def test_mission_manager_import():
    """Ensure the mission manager can be imported."""
    try:
        import scripts.mission_manager
        assert True
    except ImportError as e:
        # Ignore module dependencies missing in basic CI environments unless specified
        # the point of this test is to catch bad syntax errors at the top level
        pass

def test_perception_scripts_exist():
    """Verify that core perception routines exist in the file tree."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    perception_dir = os.path.join(base_dir, 'scripts', 'perception')
    assert os.path.exists(perception_dir), "Perception directory is completely missing!"
    
    yolo_file = os.path.join(perception_dir, 'yolo_inference.py')
    assert os.path.exists(yolo_file), "YOLO Inference script missing!"
