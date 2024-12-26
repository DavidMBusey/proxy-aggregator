import logging
import os

class Logger:
    def __init__(self, log_file="application.log"):
        # Create a logger object
        self.logger = logging.getLogger("ProxyScraperLogger")
        self.logger.setLevel(logging.DEBUG)  # Set the minimum log level

        # Create log directory if it doesn't exist
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # File handler to save logs to a file
        file_handler = logging.FileHandler(f"logs/{log_file}")
        file_handler.setLevel(logging.DEBUG)

        # Console handler to display logs in the terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Log format
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)
