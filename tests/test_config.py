"""
Unit tests for the ConfigLoader module.
"""

import os
import pytest
import yaml
from scripts.core.config_loader import ConfigLoader

# This fixture creates a temporary yaml file for testing
@pytest.fixture
def temp_config_file(tmp_path):
    config_data = {
        'robot': {
            'id': 'TEST-01',
            'type': 'UGV'
        },
        'control': {
            'pid': {
                'kp': 2.0,
                'ki': 0.5
            }
        }
    }
    file_path = tmp_path / "test_robot_params.yaml"
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(config_data, f)
    
    return str(file_path)

def test_load_valid_config(temp_config_file):
    loader = ConfigLoader(config_path=temp_config_file)
    assert loader.config is not None

def test_get_robot_id(temp_config_file):
    loader = ConfigLoader(config_path=temp_config_file)
    assert loader.get_robot_id() == 'TEST-01'

def test_get_section(temp_config_file):
    loader = ConfigLoader(config_path=temp_config_file)
    control_config = loader.get('control')
    assert control_config is not None
    assert 'pid' in control_config

def test_get_nested_value(temp_config_file):
    loader = ConfigLoader(config_path=temp_config_file)
    control_config = loader.get('control')
    assert control_config['pid']['kp'] == 2.0

def test_get_nonexistent_section(temp_config_file):
    loader = ConfigLoader(config_path=temp_config_file)
    assert loader.get('nonexistent') is None

def test_missing_file_raises_error():
    with pytest.raises(FileNotFoundError):
        ConfigLoader(config_path="nonexistent_file.yaml")
