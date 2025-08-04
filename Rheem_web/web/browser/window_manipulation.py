class WindowManipulation:
    """
    Provides methods to manipulate the browser window using Playwright,
    such as zooming, resizing, maximizing, and adjusting zoom until an element is visible.
    """

    def __init__(self, playwright_driver):
        """
        Initializes the WindowManipulation with the provided Playwright driver.

        :param playwright_driver: The Playwright driver abstraction.
        """
        self.playwright_driver = playwright_driver

    def zoom_in_out(self, in_out: str):
        """
        Zooms in, zooms out, or resets the zoom level of the browser window using JavaScript.

        :param in_out: "ADD" to zoom in, "SUBTRACT" to zoom out, "reset" to reset zoom.
        """
        page = self.playwright_driver.page
        if in_out.upper() == "ADD":
            page.evaluate("document.body.style.zoom = (parseFloat(document.body.style.zoom || 1) + 0.1).toString()")
        elif in_out.upper() == "SUBTRACT":
            page.evaluate("document.body.style.zoom = (parseFloat(document.body.style.zoom || 1) - 0.1).toString()")
        elif in_out.lower() == "reset":
            page.evaluate("document.body.style.zoom = '1'")

    def zoom_in_out_till_element_display(self, selector: str, in_out: str):
        """
        Zooms in or out until the specified element is visible.

        :param selector: The selector of the element to be located.
        :param in_out: "ADD" to zoom in, "SUBTRACT" to zoom out.
        """
        page = self.playwright_driver.page
        for _ in range(20):  # Prevent infinite loop
            if page.locator(selector).is_visible():
                break
            self.zoom_in_out(in_out)

    def resize_browser(self, width: int, height: int):
        """
        Resizes the browser window to the specified width and height.

        :param width: Desired width in pixels.
        :param height: Desired height in pixels.
        """
        self.playwright_driver.page.set_viewport_size({"width": width, "height": height})

    def maximize_browser(self):
        """
        Maximizes the browser window to the screen size.
        """
        # Playwright does not have a direct maximize, so use a large size
        self.playwright_driver.page.set_viewport_size({"width": 1920, "height": 1080})

    def zoom_in_and_out(self, value: str):
        """
        Sets the zoom level of the page using a percentage value via JavaScript.

        :param value: Desired zoom value as a string percentage (e.g., "100" for 100%).
        """
        self.playwright_driver.page.evaluate(f"document.body.style.zoom = '{value}%'")