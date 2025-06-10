from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://sbx-oncall-uat.sandbox.ngc:44343/oncall/"

    def __init__(self, page):
        super().__init__(page)
        self.username_selector = "#username"
        self.password_selector = "#password"
        self.login_button_selector = "button:has-text('Log In')"
        self.error_selector = "span.error-msg"

    def load(self):
        self.goto(self.URL)

    def login(self, username: str, password: str):
        self.fill(self.username_selector, username)
        self.fill(self.password_selector, password)
        self.click(self.login_button_selector)

    def get_error_message(self) -> str:
        return self.get_text(self.error_selector)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.error_selector)
