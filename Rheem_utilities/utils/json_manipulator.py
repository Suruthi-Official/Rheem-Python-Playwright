import json
import logging
from jsonpath_ng import parse as jsonpath_parse

class JsonManipulator:
    """
    Provides methods for reading, writing, updating, and deleting JSON data.
    Uses Python's json module and jsonpath-ng for querying JSON data.
    """
    LOGGER = logging.getLogger("JsonManipulator")

    def __init__(self, json_str):
        try:
            self.json = json.loads(json_str)
        except Exception as e:
            self.LOGGER.error(f"Error during JsonManipulator initialization. Defaulting to empty JSON object: {e}")
            self.json = {}

    def read(self, json_path):
        try:
            jsonpath_expr = jsonpath_parse(json_path)
            matches = [match.value for match in jsonpath_expr.find(self.json)]
            if not matches:
                return None
            return matches[0] if len(matches) == 1 else matches
        except Exception as e:
            raise RuntimeError(f"Error when reading JSON path {json_path}") from e

    def delete(self, json_path):
        try:
            jsonpath_expr = jsonpath_parse(json_path)
            for match in jsonpath_expr.find(self.json):
                self._delete_at_path(match.full_path)
        except Exception as e:
            raise RuntimeError(f"Error when deleting path {json_path}") from e

    def write_or_update(self, json_path, value):
        try:
            jsonpath_expr = jsonpath_parse(json_path)
            matches = list(jsonpath_expr.find(self.json))
            if matches:
                for match in matches:
                    self._set_at_path(match.full_path, value)
            else:
                self._set_at_path(jsonpath_expr, value)
        except Exception as e:
            raise RuntimeError("Error when writing or updating the JSON using JsonPath.") from e

    def _set_at_path(self, path_expr, value):
        # Only supports setting at root or simple paths for brevity
        # For more complex paths, a full implementation is needed
        if hasattr(path_expr, 'fields') and path_expr.fields:
            current = self.json
            for field in path_expr.fields[:-1]:
                if field not in current or not isinstance(current[field], dict):
                    current[field] = {}
                current = current[field]
            current[path_expr.fields[-1]] = value
        else:
            self.json = value

    def _delete_at_path(self, path_expr):
        # Only supports deleting at root or simple paths for brevity
        if hasattr(path_expr, 'fields') and path_expr.fields:
            current = self.json
            for field in path_expr.fields[:-1]:
                if field not in current:
                    return
                current = current[field]
            current.pop(path_expr.fields[-1], None)

    def __str__(self):
        return json.dumps(self.json)
