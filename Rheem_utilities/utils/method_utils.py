import logging
import time

class MethodUtils:
    """
    Provides utility methods for executing callables with retry mechanisms.
    This class cannot be instantiated.
    """
    LOGGER = logging.getLogger("MethodUtils")

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("MethodUtils class cannot be instantiated.")

    @staticmethod
    def execute_with_retry(supplier, max_retries, max_backoff_millis):
        """
        Executes a given supplier function with a specified number of retry attempts and exponential backoff.
        :param supplier: Callable with no arguments.
        :param max_retries: int, number of retries.
        :param max_backoff_millis: int, max backoff in milliseconds.
        :return: result of supplier() if successful.
        :raises RuntimeError: if all retries are exhausted.
        """
        for i in range(max_retries):
            try:
                return supplier()
            except Exception as e:
                MethodUtils.LOGGER.warning(f"Execution failure detected. Retrying... ({i + 1}/{max_retries})")
                if i == max_retries - 1:
                    MethodUtils.LOGGER.error("All execution retry attempts exhausted.", exc_info=e)
                    raise RuntimeError(e)
                backoff_time = min(2 ** i * 1_000, max_backoff_millis) / 1000.0
                try:
                    time.sleep(backoff_time)
                except Exception:
                    pass
        return None  # should not reach here
