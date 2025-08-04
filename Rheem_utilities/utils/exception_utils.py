import logging
from typing import Callable, Any

class ExceptionUtils:
    """
    Provides utility methods for logging errors and throwing exceptions.
    This class cannot be instantiated.
    """
    LOGGER = logging.getLogger("ExceptionUtils")

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("ExceptionUtils class cannot be instantiated.")

    @staticmethod
    def log_error_and_throw_if_null(object_to_check: Any, obj_name: str = "Unnamed object", logger: logging.Logger = None):
        if object_to_check is None:
            logger = logger or ExceptionUtils.LOGGER
            logger.error(f"{obj_name} cannot be null.")
            raise ValueError(f"{obj_name} is null.")

    @staticmethod
    def log_error_and_throw(logger: logging.Logger, message: str, exception_supplier: Callable[[], Exception]):
        exception = exception_supplier()
        ExceptionUtils.log_error_and_throw_with_exception(logger, message, exception)

    @staticmethod
    def log_error_and_throw_with_exception(logger: logging.Logger, message: str, exception: Exception):
        logger.error(f"{message}: {exception}")
        raise RuntimeError(message) from exception

    @staticmethod
    def log_error_and_throw_supplier(exception_supplier: Callable[[], Exception]):
        ExceptionUtils.log_error_and_throw(ExceptionUtils.LOGGER, "", exception_supplier)
