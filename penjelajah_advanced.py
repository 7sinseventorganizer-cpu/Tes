# Advanced Explorer Agent

class AdvancedExplorer:
    def __init__(self, config_directory):
        self.config_directory = config_directory

    def find_config_files(self):
        """Step 1: Find configuration files in the directory."""
        import os
        config_files = [f for f in os.listdir(self.config_directory) if f.endswith('.conf') or f.endswith('.json')]
        return config_files

    def read_contents(self, config_files):
        """Step 2: Read contents of the found configuration files."""
        contents = {}
        for file_name in config_files:
            with open(os.path.join(self.config_directory, file_name), 'r') as file:
                contents[file_name] = file.read()
        return contents

    def parse_structured_format(self, contents):
        """Step 3: Parse the structured format of the contents."""
        import json
        parsed_data = {}
        for file_name, content in contents.items():
            try:
                parsed_data[file_name] = json.loads(content)
            except json.JSONDecodeError:
                # handle non-JSON formats if needed
                continue
        return parsed_data

    def find_internal_keys(self, parsed_data):
        """Step 4: Find internal keys within the parsed data."""
        internal_keys = []
        for data in parsed_data.values():
            if isinstance(data, dict):
                internal_keys.extend(data.keys())
        return internal_keys

    def unwrap_layers(self, parsed_data):
        """Step 5: Unwrap layers in the structured data to find nested content."""
        unwrapped = {}
        for data in parsed_data.values():
            # Example logic to unwrap layers based on depth
            unwrapped.update(data)
        return unwrapped

    def prepare_recognizable_keys(self, unwrapped_data):
        """Step 6: Prepare recognizable keys for further processing."""
        recognizable_keys = {k: v for k, v in unwrapped_data.items() if isinstance(v, str)}
        return recognizable_keys

# Example usage:
# explorer = AdvancedExplorer('/path/to/configs')
# config_files = explorer.find_config_files()
# contents = explorer.read_contents(config_files)
# parsed_data = explorer.parse_structured_format(contents)
# internal_keys = explorer.find_internal_keys(parsed_data)
# unwrapped_data = explorer.unwrap_layers(parsed_data)
# recognizable_keys = explorer.prepare_recognizable_keys(unwrapped_data)