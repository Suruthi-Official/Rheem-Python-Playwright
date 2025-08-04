class Fill_keys:
    """
    Provides methods for sending keyboard inputs to a web element using Playwright.
    Allows sending plain text, pressing specific keys, and handling key combinations.
    """

    def __init__(self, playwrightdriver):
        """
        Initialize with a Playwright Page instance.

        :param page: Playwright Page object.
        """
        self.playwrightdriver = playwrightdriver

    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).

        :param obj: CSS selector (str) or Locator.
        :return: Locator
        """
        if isinstance(obj, str):
            return self.playwrightdriver.page.locator(obj)
        return obj


    def enter_keys(self, obj, key: str):
        """
        Alias for enter_key for compatibility.

        :param obj: Selector (str) or Locator for the element.
        :param key: The key to be pressed.
        """
        self.enter_key(obj, key)

    def enter_key_combinations(self, obj, keystrings):
        """
        Sends a combination of keys (e.g., ["Shift", "Enter"]) to a web element.

        :param obj: Selector (str) or Locator for the element.
        :param keystrings: List of strings representing the key combinations.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        # Playwright supports pressing key combinations as a string like "Shift+Enter"
        combo = "+".join(keystrings)
        locator.press(combo)

    def hit_key_combinations(self, keystrings):
        """
        Sends a combination of keys globally (not bound to any specific web element).

        :param keystrings: List of strings representing the key combinations.
        """
        combo = "+".join(keystrings)
        self.playwrightdriver.page.keyboard.press(combo)