class TabEvent:
    """
    The TabEvent class provides methods to interact with browser tabs,
    such as creating a new tab, switching between tabs, and switching to the first tab.
    It relies on Playwright to manipulate browser pages (tabs).
    """

    def __init__(self, playwright_driver):
        """
        Initializes TabEvent with a Playwright driver instance.

        :param playwright_driver: The Playwright driver instance.
        """
        self.playwright_driver = playwright_driver

    def create_new(self, url: str):
        """
        Creates a new browser tab and navigates to the specified URL.

        :param url: The URL to navigate to in the newly opened tab.
        """
        new_page = self.playwright_driver.context.new_page()
        new_page.goto(url)
        self.playwright_driver.page = new_page  # Optionally set as active page
        # WebAppDriver.WebAppDriver.set_page(self.playwright_driver.page)

    def switch_to(self, tab_title: str):
        """
        Switches to a tab based on the tab's title.

        :param tab_title: The title of the tab to switch to.
        """
        for page in self.playwright_driver.context.pages:
            if page.title().lower() == tab_title.lower():
                self.playwright_driver.page = page
                break

    def switch_to_first_tab(self):
        """
        Switches to the first tab in the browser.
        """
        first_page = self.playwright_driver.context.pages[0]
        self.playwright_driver.page = first_page

    def switch_to_new_tab(self):
        """
        Switches to the most recently opened tab.
        """
        pages = self.playwright_driver.context.pages
        if pages:
            self.playwright_driver.page = pages[-1]

    def close_current_tab(self):
        """
        Closes the currently active tab.
        """
        if self.playwright_driver.page:
            self.playwright_driver.page.close()
        else:
            raise Exception("No active tab to close.")
