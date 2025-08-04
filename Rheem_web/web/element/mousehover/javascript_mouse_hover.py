from playwright.sync_api import Page, Locator
import time

class JavaScriptMouseHover:
    """
    Provides a method to simulate a mouse hover over an element using JavaScript in Playwright.
    Accepts either a selector string or a Locator.
    """

    def __init__(self, page: Page):
        """
        Initialize with a Playwright Page instance.
        :param page: Playwright Page object.
        """
        self.page = page

    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        :param obj: CSS selector (str) or Locator.
        :return: Locator
        """
        if isinstance(obj, str):
            return self.page.locator(obj)
        return obj

    def mouse_hover(self, obj, sleep_seconds=5):
        """
        Simulates a mouse hover over the specified element using JavaScript.
        Dispatches a 'mouseover' event.
        :param obj: Selector (str) or Locator for the element.
        :param sleep_seconds: Seconds to wait after hover (default 5).
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.evaluate("""
            el => {
                if (document.createEvent) {
                    var evObj = document.createEvent('MouseEvents');
                    evObj.initEvent('mouseover', true, false);
                    el.dispatchEvent(evObj);
                } else if (document.createEventObject) {
                    el.fireEvent('onmouseover');
                }
            }
        """)
        time.sleep(sleep_seconds)