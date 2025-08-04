import os
from datetime import datetime
from functools import wraps

class Trace_logs:
    def __init__(self, playwright_driver):
        self.playwright_driver = playwright_driver
        self.trace_file_path = None

    def start_trace(self):
        context = self.playwright_driver.get_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    def end_trace(self, method_name):
        context = self.playwright_driver.get_context()
        now = datetime.now()
        date_folder = now.strftime("%Y%m%d")
        timestamp = now.strftime("%H%M%S")
        directory = os.path.join("test_results", date_folder)
        os.makedirs(directory, exist_ok=True)
        file_name = f"{method_name}_{timestamp}_trace.zip"
        self.trace_file_path = os.path.join(directory, file_name)
        context.tracing.stop(path=self.trace_file_path)

    @staticmethod
    def trace_test(method_name):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                self.driver.trace_logs.start_trace()
                try:
                    return func(self, *args, **kwargs)
                finally:
                    self.driver.trace_logs.end_trace(method_name)
            return wrapper
        return decorator
