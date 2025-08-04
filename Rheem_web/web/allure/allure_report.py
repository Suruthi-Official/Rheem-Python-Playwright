from pathlib import Path
import allure
class Allure_report:
        def __init__(self, playwright_driver):
            self.playwright_driver = playwright_driver


        def allure_screenshot(self, execute: bool):
            if execute:
                # Capture the screenshot
                png_bytes = self.playwright_driver.page.screenshot()
                
                # Save the screenshot to a file
                screenshot_path = Path("full-page.png")
                screenshot_path.write_bytes(png_bytes)
                
                # Attach the screenshot to Allure report
                allure.attach.file(
                    str(screenshot_path),
                    name="full-page",
                    attachment_type=allure.attachment_type.PNG
                )
                print("Screenshot captured and attached to Allure report.")
            else:
                print("Screenshot capture skipped.")