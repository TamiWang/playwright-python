from pages.base_page import BasePage

class InitializingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.initializing_text_selector = "text=Initializing..."
        self.copyright_selector = "text=HEXAGON"

    def wait_for_initializing_page(self, timeout: int = 10000):
        self.wait_until_visible(self.initializing_text_selector, timeout)

    def is_initializing_displayed(self) -> bool:
        return self.is_visible(self.initializing_text_selector)
