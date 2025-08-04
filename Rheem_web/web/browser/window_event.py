class WindowEvent:
    """
    Handles browser window, tab, alert, and frame interactions using Playwright.
    """

    def __init__(self, playwright_driver):
        """
        Initializes the WindowEvent with the provided Playwright driver.

        :param playwright_driver: The Playwright driver abstraction.
        """
        self.playwright_driver = playwright_driver
        self.old_page = None
        self.last_page = None

    def handle_alert(self, decision: str):
        """
        Handles an alert by either accepting or dismissing it.

        :param decision: "accept" or "dismiss".
        """
        def dialog_handler(dialog):
            if decision.lower() == "accept":
                dialog.accept()
            else:
                dialog.dismiss()
            self.playwright_driver.page.off("dialog", dialog_handler)
        self.playwright_driver.page.once("dialog", dialog_handler)

    def get_alert_text(self) -> str:
        """
        Retrieves the text of the current alert.

        :return: The text of the alert.
        """
        alert_text = {}

        def dialog_handler(dialog):
            alert_text["text"] = dialog.message
            dialog.dismiss()
            self.playwright_driver.page.off("dialog", dialog_handler)
        self.playwright_driver.page.once("dialog", dialog_handler)
        # Trigger the alert in your test before calling this method
        return alert_text.get("text", "")

    def switch_to_new_window(self):
        """
        Switches to the most recently opened window or tab.
        """
        self.old_page = self.playwright_driver.page
        pages = self.playwright_driver.context.pages
        self.last_page = pages[-1]
        self.playwright_driver.page = self.last_page

    def switch_to_old_window(self):
        """
        Switches back to the original window or tab.
        """
        if self.old_page:
            self.playwright_driver.page = self.old_page

    def switch_to_new_tab(self):
        """
        Switches to the most recently opened tab.
        """
        self.switch_to_new_window()

    def switch_to_old_tab(self):
        """
        Switches back to the original tab.
        """
        self.switch_to_old_window()

    def switch_to_window_by_title(self, window_title: str):
        """
        Switches to a window based on the specified window title.

        :param window_title: The title of the window to switch to.
        :raises Exception: If no window with the given title is found.
        """
        self.old_page = self.playwright_driver.page
        found = False
        for page in self.playwright_driver.context.pages:
            if page.title() == window_title:
                self.playwright_driver.page = page
                found = True
                break
        if not found:
            raise Exception(f"Window with title {window_title} not found")

    def close_new_window(self):
        """
        Closes the most recently opened window and returns to the main window.
        """
        if self.last_page:
            self.last_page.close()
            self.switch_to_old_window()

    def switch_frame(self, frame_name_or_selector):
        """
        Switches to a frame identified by name or selector.

        :param frame_name_or_selector: The name or selector of the frame.
        """
        frame = self.playwright_driver.page.frame(name=frame_name_or_selector)
        if not frame:
            frame = self.playwright_driver.page.frame_locator(frame_name_or_selector).frame()
        self.playwright_driver.frame = frame

    def switch_to_default_content(self):
        """
        Switches to the default content of the page, leaving any frames.
        """
        self.playwright_driver.frame = self.playwright_driver.page.main_frame

    def refresh_page(self):
        """
        Refreshes the current page in the browser.
        """
        self.playwright_driver.page.reload()

    def create_new_window(self, url: str):
        """
        Creates a new browser window and navigates to the specified URL.

        :param url: The URL to navigate to in the new window.
        """
        self.old_page = self.playwright_driver.page
        new_page = self.playwright_driver.context.new_page()
        new_page.goto(url)
        self.playwright_driver.page = new_page

    def close_current_window(self):
        """
        Closes the current window.
        """
        if self.playwright_driver.page:
            self.playwright_driver.page.close()
        else:
            raise Exception("No current window to close.")