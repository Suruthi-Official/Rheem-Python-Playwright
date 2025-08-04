from enum import Enum

class BrowserType(Enum):
    """
    Enum representing the supported browser types.
    """
    CHROME = 1
    FIREFOX = 2
    SAFARI = 3
    EDGE = 4
    DEFAULT = 5

class ManipulationMode(Enum):
    """
    Enum representing the types of manipulation operations that can be performed.
    """
    SET = 1
    UPDATE = 2
    DELETE = 3

class ComparisonType(Enum):
    """
    Enum representing the types of comparison operations that can be used in conditions or assertions.
    """
    EQUAL = 1
    NOT_EQUAL = 2
    LESS_THAN = 3
    LESS_THAN_OR_EQUAL = 4
    GREATER_THAN = 5
    GREATER_THAN_OR_EQUAL = 6
    CONTAINS = 7
    NOT_CONTAINS = 8
    STARTS_WITH = 9
    HAS_ITEM = 10
    NOT_HAS_ITEM = 11
    IS_EMPTY = 12
    IS_NOT_EMPTY = 13
    IS_NULL = 14
    IS_NOT_NULL = 15
    IS_TRUE = 16
    IS_FALSE = 17
    IS_NUMBER = 18
