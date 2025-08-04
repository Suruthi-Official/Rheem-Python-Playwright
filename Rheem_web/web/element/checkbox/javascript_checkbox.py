class JavaScriptCheckBox:
    """
    Provides actions to interact with checkboxes on a webpage using JavaScript execution in Playwright.
    Includes methods to check, uncheck, and toggle checkbox elements.
    """

    def __init__(self, playwrightdriver):
        """
        Initializes the JavaScriptCheckBox with a Playwright Page instance.
        :param page: The Playwright Page object.
        """
        self.driver = playwrightdriver

    def check(self, selector: str):
        """
        Checks a checkbox using JavaScript if it is not already checked.
        :param selector: The selector for the checkbox element.
        """
        self.playwrightdriver.page.wait_for_selector(selector, state="visible")
        self.playwrightdriver.page.eval_on_selector(
            selector,
            "checkbox => { if (!checkbox.checked) { checkbox.checked = true; } }"
        )

    def uncheck(self, selector: str):
        """
        Unchecks a checkbox using JavaScript if it is checked.
        :param selector: The selector for the checkbox element.
        """
        self.playwrightdriver.page.wait_for_selector(selector, state="visible")
        self.playwrightdriver.page.eval_on_selector(
            selector,
            "checkbox => { if (checkbox.checked) { checkbox.checked = false; } }"
        )

    def toggle(self, selector: str):
        """
        Toggles a checkbox using JavaScript.
        :param selector: The selector for the checkbox element.
        """
        self.playwrightdriver.page.wait_for_selector(selector, state="visible")
        self.playwrightdriver.page.eval_on_selector(
            selector,
            "checkbox => { checkbox.checked = !checkbox.checked; }"
        )