import logging
import os
from Rheem_web.web.config import web_constants

class LoggerUtils:
    _loggers = {}
    @staticmethod
   
    def setup_logger(name, log_file=None, level=web_constants.LOG_LEVEL):
        """
        Set up a logger with the specified name, log file, and logging level.

        Returns:
        - logger (logging.Logger): Configured logger instance.
        """
        log_levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }

        if level is None:
            level = web_constants.LOG_LEVEL  # Default to WebConstants.LOG_LEVEL if no level is provided

        # Convert string level to logging level constant
        level = log_levels.get(level, logging.INFO)
        # Check if the logger already exists
        if name in LoggerUtils._loggers:
            return LoggerUtils._loggers[name]

        # Create a logger with the specified name
        logger = logging.getLogger(name)

        # Set the logging level
        logger.setLevel(level)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # If a log file is specified, create a file handler
        if log_file:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_formatter = logging.Formatter(
                '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        # Store the logger instance
        LoggerUtils._loggers[name] = logger
        return logger

    def __init__(self, name=__name__, log_file=None, level=logging.INFO):
        """
        Initialize the Logger and set up the logger.

        Parameters:
        - name (str): The name of the logger (default is the module name).
        - log_file (str): The file to which logs should be written (optional).
        - level : The logging level (default is logging.INFO).
        """
        self.logger = LoggerUtils.setup_logger(name, log_file, level)

    def info(self, message):
        """Log an info message."""
        self.logger.info(message)

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message):
        """Log a critical message."""
        self.logger.critical(message)

# Example usage:
# logger_instance = Logger(log_file='app.log')
# logger_instance.info("This is an info message.")
# logger_instance.debug("This is a debug message.")
