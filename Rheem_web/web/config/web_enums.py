from enum import Enum, auto

class BrowserType(Enum):
    """
    Enum representing the supported browser types for the framework.
    """
    CHROME = "chromium"
    FIREFOX = "firefox"
    EDGE = "edge"
    SAFARI = "webkit"
    CHROME_CANARY = "chrome-canary"
    DEFAULT = "default"
