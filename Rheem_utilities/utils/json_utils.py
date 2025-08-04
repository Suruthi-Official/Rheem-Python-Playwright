import json
import logging

class JsonUtils:
    """
    Provides utility methods for JSON operations such as converting objects to JSON strings.
    This class cannot be instantiated.
    """
    LOGGER = logging.getLogger("JsonUtils")

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("JsonUtils class cannot be instantiated.")

    @staticmethod
    def to_json(obj):
        if obj is None:
            return "null"
        try:
            return json.dumps(obj)
        except Exception as e:
            JsonUtils.LOGGER.error("Error during conversion of Object to JSON string: %s", e)
            return '"serialization_error"'
