class WindowScrolling:
    """
    Provides methods to manipulate the scrolling behavior of a web page using Playwright.
    Allows scrolling to the top, bottom, specific elements, or by specific pixel amounts.
    """

    def __init__(self, playwright_driver):
        """
        Initializes the WindowScrolling with the provided Playwright driver.

        :param playwright_driver: The Playwright driver abstraction.
        """
        self.playwright_driver = playwright_driver

    def scroll_to_end(self):
        """
        Scrolls to the bottom of the page.
        """
        self.playwright_driver.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        """
        Scrolls to the top of the page.
        """
        self.playwright_driver.page.evaluate("window.scrollTo(0, 0)")

    def scroll_to_element(self, selector: str):
        """
        Scrolls to the specific element on the page.

        :param selector: The selector of the element to scroll to.
        """
        locator = self.playwright_driver.page.locator(selector)
        locator.scroll_into_view_if_needed()

    def scroll_vertical_pixels(self, pixels_to_scroll: int):
        """
        Scrolls the window vertically by a specified number of pixels.

        :param pixels_to_scroll: Number of pixels to scroll vertically.
        """
        self.playwright_driver.page.evaluate(f"window.scrollBy(0, {pixels_to_scroll})")

    def scroll_horizontal_pixels(self, pixels_to_scroll: int):
        """
        Scrolls the window horizontally by a specified number of pixels.

        :param pixels_to_scroll: Number of pixels to scroll horizontally.
        """
        self.playwright_driver.page.evaluate(f"window.scrollBy({pixels_to_scroll}, 0)")