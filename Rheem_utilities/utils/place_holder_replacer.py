import re

class PlaceHolderReplacer:
    """
    Utility class to replace placeholders in a given string with their corresponding values
    from a provided map. Placeholders are defined in the format `${placeholder}`.
    """
    PLACEHOLDER_PATTERN = re.compile(r"\$\{([^}]+)}")

    def __init__(self, input_map):
        # Convert keys to lowercase for case-insensitive matching
        self.input_map = {str(k).lower(): str(v) for k, v in input_map.items()}
        self.replace_unknown = False

    def replace(self, input_str):
        if input_str is None or "${" not in input_str:
            return input_str
        def repl(match):
            variable = match.group(1)
            return self.get_replacement(variable)
        return self.PLACEHOLDER_PATTERN.sub(repl, input_str)

    def get_replacement(self, variable):
        variable = variable.lower()
        replacement = self.input_map.get(variable)
        if replacement is None:
            if self.replace_unknown:
                return "VALUE_NOT_SET"
            else:
                return f"${{{variable}}}"
        return replacement

    def set_replace_unknown(self, replace_unknown):
        self.replace_unknown = replace_unknown
