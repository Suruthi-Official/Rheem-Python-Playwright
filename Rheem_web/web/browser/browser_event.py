class BrowserEvent:
    """
    The BrowserEvent class encapsulates browser navigation actions such as going to a URL,
    navigating back, forward, and refreshing the page.
    It interacts with a PlaywrightDriver instance to perform these actions on the browser.
    """

    def __init__(self, playwrightdriver):
        """
        Initializes the BrowserEvent with a PlaywrightDriver instance.

        :param playwright_driver: The PlaywrightDriver instance used to interact with the browser.
        """
        self.playwrightdriver = playwrightdriver

    def go_to_url(self, url: str):
        """
        Navigates to the specified URL in the browser.

        :param url: The URL to navigate to.
        """
        self.playwrightdriver.page.goto(url)

    def wait_for_url_load(self,url):
        self.playwrightdriver.page.wait_for_url(url)

    def go_to_url_by_po_value(self, obj_name: str):
        """
        Navigates to the URL specified by a page object value.
        This method retrieves the URL value from the page object map using the specified object name.

        :param obj_name: The name of the page object whose value holds the URL to navigate to.
        """
        url = self.playwright_driver.get_page_objects().get(obj_name, "value")
        self.go_to_url(url)

    def back(self):
        """
        Navigates back in the browser history.
        Equivalent to clicking the browser's back button.
        """
        self.playwrightdriver.page.go_back()

    def forward(self):
        """
        Navigates forward in the browser history.
        Equivalent to clicking the browser's forward button.
        """
        self.playwrightdriver.page.go_forward()

    def refresh(self):
        """
        Refreshes the current page in the browser.
        Equivalent to clicking the browser's refresh button or pressing F5.
        """
        self.playwrightdriver.page.reload()
 