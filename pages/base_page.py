class BasePage:
    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(10000)  # 10 seconds default timeout
        self.page.set_default_navigation_timeout(15000)  # For navigations

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str, timeout: int = 5000):
        self.page.locator(selector).click(timeout=timeout)

    def fill(self, selector: str, value: str, timeout: int = 5000):
        self.page.locator(selector).fill(value, timeout=timeout)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()
    
    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
    
    def is_enabled(self, selector: str) -> bool:
        return self.page.locator(selector).is_enabled()

    def wait_until_visible(self, selector: str, timeout: int = 5000):
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    def wait_until_enabled(self, selector: str, timeout: int = 5000):
        self.page.locator(selector).wait_for(state="attached", timeout=timeout)
