import os

class PropUtils:
    """
    Utility class for managing properties files.
    Provides methods to read, write, and manipulate key-value pairs in a properties file.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.properties = {}
        self._load_properties()

    def _load_properties(self):
        if not os.path.exists(self.file_path):
            return
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if '=' in line:
                        key, value = line.split('=', 1)
                        self.properties[key.strip()] = value.strip()
        except Exception:
            pass

    def get(self, name):
        return self.properties.get(name)

    def get_all_properties(self):
        return dict(self.properties)

    def get_as_map(self):
        return dict(self.properties)

    def set(self, name, value):
        self.properties[name] = value
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                for k, v in self.properties.items():
                    f.write(f"{k}={v}\n")
        except Exception:
            pass
