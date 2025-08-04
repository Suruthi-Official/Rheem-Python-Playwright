import logging
from enum import Enum

class ManipulationMode(Enum):
    SET = 'SET'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'

class MapUtils:
    """
    Provides utility methods for operations on dicts, such as converting, updating, and merging dicts.
    This class cannot be instantiated.
    """
    LOGGER = logging.getLogger("MapUtils")

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("MapUtils class cannot be instantiated.")

    @staticmethod
    def convert_to_map_str_str(input_map):
        if input_map is None:
            MapUtils.LOGGER.warning("Input Map is null. Returning empty dict.")
            return {}
        try:
            return {str(k): str(v) for k, v in input_map.items()}
        except Exception as e:
            MapUtils.LOGGER.error("Error converting dict to dict[str, str] in convert_to_map_str_str method: %s", e)
            raise RuntimeError("Error converting dict") from e

    @staticmethod
    def data_table_to_map(data_table):
        if data_table is None:
            MapUtils.LOGGER.warning("Data table is null. Returning empty dict.")
            return {}
        rows = data_table
        # Expecting rows as List[List[str]]
        MapUtils.LOGGER.debug(f"Rows of data table: {rows}")
        result = {}
        for row in rows:
            if len(row) >= 2:
                result[row[0]] = row[1]
            elif len(row) == 1:
                result[row[0]] = None
            else:
                MapUtils.LOGGER.error("Row in the DataTable is empty")
                raise ValueError("Row in the DataTable is empty")
        return result

    @staticmethod
    def update_map(mode, input_map, map_to_update):
        if mode is None:
            raise ValueError("Mode cannot be null.")
        if map_to_update is None:
            MapUtils.LOGGER.debug("Map to update is null. Initializing new dict.")
            map_to_update = {}
        updated_map = dict(map_to_update)
        if input_map is None:
            MapUtils.LOGGER.debug("Input Map is null. No changes made to Map to update.")
            return updated_map
        if mode == ManipulationMode.SET:
            updated_map.clear()
            updated_map.update(input_map)
        elif mode == ManipulationMode.UPDATE:
            updated_map.update(input_map)
        elif mode == ManipulationMode.DELETE:
            for key in input_map.keys():
                updated_map.pop(key, None)
        else:
            MapUtils.LOGGER.error(f"Unsupported mode argument for update_map method: {mode}")
            raise ValueError(f"Unsupported mode: {mode}")
        return updated_map
