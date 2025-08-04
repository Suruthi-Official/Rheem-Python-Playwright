import json

class StringToType:
    """
    Utility methods to convert string representations of values to their respective data types.
    This class cannot be instantiated.
    """
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("StringToType class cannot be instantiated.")

    @staticmethod
    def parse_value(typed_value):
        if typed_value.endswith((':string', ':str')):
            return typed_value[:typed_value.rfind(":")]
        elif typed_value.endswith((':bool', ':boolean')):
            return typed_value[:typed_value.rfind(":")].lower() == 'true'
        elif typed_value.endswith((':int', ':integer')):
            return int(typed_value[:typed_value.rfind(":")])
        elif typed_value.endswith((':float', ':double', ':decimal')):
            return float(typed_value[:typed_value.rfind(":")])
        elif typed_value.endswith(':long'):
            return int(typed_value[:typed_value.rfind(":")])
        elif typed_value.endswith(':null'):
            return None
        elif typed_value.endswith(':json'):
            json_str = typed_value[:typed_value.rfind(":json")]
            try:
                return json.loads(json_str)
            except Exception as e:
                raise RuntimeError(f"Error parsing JSON value: {json_str}") from e
        else:
            return typed_value
