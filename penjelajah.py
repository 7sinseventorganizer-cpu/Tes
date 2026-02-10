# Penjelajah (Explorer) Agent

"""
The Explorer agent is designed to find and parse configuration files in a directory structure.
It will search through all subdirectories, identify files with specific extensions that denote configuration files,
read their contents, and return a structured representation of these configurations.
"""

import os
import json
import yaml
from typing import Dict, List, Any

class Penjelajah:
    def __init__(self, search_path: str, extensions: List[str] = None):
        self.search_path = search_path
        self.extensions = extensions if extensions else ['.json', '.yaml', '.yml']
        self.configurations = {}

    def find_config_files(self) -> List[str]:
        found_files = []
        for root, dirs, files in os.walk(self.search_path):
            for file in files:
                if any(file.endswith(ext) for ext in self.extensions):
                    found_files.append(os.path.join(root, file))
        return found_files

    def parse_config_file(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r') as file:
            if file_path.endswith('.json'):
                return json.load(file)
            elif file_path.endswith(('.yaml', '.yml')):
                return yaml.safe_load(file)
        return {}  # Return empty dict if parsing fails

    def load_configurations(self) -> Dict[str, Any]:
        config_files = self.find_config_files()
        for config_file in config_files:
            self.configurations[config_file] = self.parse_config_file(config_file)
        return self.configurations

# Example usage:
# explorer = Penjelajah('/path/to/search')
# configurations = explorer.load_configurations()
# print(configurations)  
