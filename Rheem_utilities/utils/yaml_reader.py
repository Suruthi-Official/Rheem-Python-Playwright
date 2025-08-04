import os
import yaml
import json

class YamlReader:
    """
    Utility class for reading and processing YAML files.
    Provides methods to read YAML data from files or directories,
    and to convert YAML data to JSON format.
    """
    def __init__(self):
        pass

    def get_yaml_data_from_folder(self, folder_path):
        if folder_path is None:
            raise ValueError("Folder path cannot be null")
        data = {}
        if not os.path.exists(folder_path):
            return data
        files = [f for f in os.listdir(folder_path) if f.endswith('.yml') or f.endswith('.yaml')]
        if not files:
            return data
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    yaml_data = yaml.safe_load(f)
                    if yaml_data:
                        data.update(yaml_data)
            except Exception:
                pass
        return data

    def get_yaml_data_from_file(self, file_path):
        if file_path is None:
            raise ValueError("File path cannot be null")
        if not os.path.isfile(file_path):
            return {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception:
            return {}

    def convert_yaml_data_to_json(self, yaml_data):
        if yaml_data is None:
            raise ValueError("YAML data cannot be null")
        try:
            return json.dumps(yaml_data, indent=2)
        except Exception:
            return None

    def convert_yaml_string_to_json(self, yaml_string):
        if yaml_string is None:
            raise ValueError("YAML string cannot be null")
        try:
            yaml_data = yaml.safe_load(yaml_string)
            return self.convert_yaml_data_to_json(yaml_data)
        except Exception as e:
            raise RuntimeError("Error converting YAML string to JSON") from e
