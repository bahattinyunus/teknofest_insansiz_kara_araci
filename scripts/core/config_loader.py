"""
Configuration Loader Module
Parses and loads the robot_params.yaml for use across the Gökbörü system.
"""

import os
import yaml
import logging

logger = logging.getLogger(__name__)

class ConfigLoader:
    def __init__(self, config_path=None):
        if config_path is None:
            # Default to the config directory relative to the repository root
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            self.config_path = os.path.join(base_dir, 'config', 'robot_params.yaml')
        else:
            self.config_path = config_path

        self.config = self._load_config()

    def _load_config(self):
        """Loads and parses the YAML configuration file."""
        if not os.path.exists(self.config_path):
            logger.error(f"Configuration file not found at: {self.config_path}")
            raise FileNotFoundError(f"Config file missing: {self.config_path}")
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            logger.error(f"Error parsing configuration file: {exc}")
            raise

    def get(self, section, key=None, default=None):
        """
        Retrieves a configuration value.
        If 'key' is provided, fetches the specific key within the 'section'.
        If only 'section' is provided, returns the entire section dictionary.
        """
        if self.config is None:
            return default

        section_data = self.config.get(section)

        if section_data is None:
            return default

        if key is None:
            return section_data

        return section_data.get(key, default)

    def get_robot_id(self):
        return self.get('robot', 'id', 'UNKNOWN')

if __name__ == "__main__":
    # Test execution
    logging.basicConfig(level=logging.INFO)
    loader = ConfigLoader()
    print(f"Loaded config for robot: {loader.get_robot_id()}")
    print(f"PID Kp: {loader.get('control', 'kp')}")
