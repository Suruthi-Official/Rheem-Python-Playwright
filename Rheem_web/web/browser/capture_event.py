import os
from datetime import datetime


try:
    from PIL import ImageGrab
except ImportError:
    ImageGrab = None

class CaptureEvent:
    """
    This class provides methods to capture screenshots of the browser and the desktop.
    """

    def __init__(self, playwright_driver):
        """
        Constructor for CaptureEvent.

        :param playwright_driver: The Playwright driver instance used to interact with the browser.
        """
        self.playwright_driver = playwright_driver

    def capture_screenshot(self):
        """
        Captures a screenshot of the current browser window and saves it to a specified directory.
        The screenshot filename includes a timestamp to ensure uniqueness.
        """
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        folder_name = now.strftime("%Y%m%d")
        directory = f"target/Screenshots/{folder_name}"
        os.makedirs(directory, exist_ok=True)
        file_path = f"{directory}/screenshot_{timestamp}.png"
        self.playwright_driver.page.screenshot(path=file_path)

    def capture_desktop_screenshot(self):
        """
        Captures a screenshot of the entire desktop and saves it to a specified directory.
        The screenshot filename includes a timestamp to ensure uniqueness.
        """
        if ImageGrab is None:
            raise RuntimeError("PIL.ImageGrab is required for desktop screenshots.")
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        folder_name = now.strftime("%Y%m%d")
        directory = f"target/Screenshots/{folder_name}"
        os.makedirs(directory, exist_ok=True)
        file_path = f"{directory}/desktop_screenshot_{timestamp}.png"
        img = ImageGrab.grab()
        img.save(file_path, "PNG") 


