from pages.base_page import BasePage

class DispatchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.position_selector = "#PositionSelector"
        self.language_selector = "div.label:has-text('Language') + div select"
        self.continue_button_selector = "button:has-text('Continue')"
        self.position_label_selector = "div.label:has-text('Position')"

    def wait_for_position_selector(self, timeout: int = 5000):
        """Wait for the Position dropdown to become visible."""
        self.wait_until_visible(self.position_selector, timeout)

    def select_position_by_text(self, text: str):
        """Click dropdown and choose option by visible text."""
        self.click(self.position_selector)
        self.click(f"text={text}")  # You could also use select_option if <select>

    def select_language_by_text(self, text: str):
        self.page.select_option("select", label=text)  # Not wrapped because it's a form select

    def click_continue(self):
        self.click(self.continue_button_selector)

    def is_position_visible(self, timeout=5000) -> bool:
        try:
            self.wait_until_visible(self.position_selector, timeout)
            return True
        except:
            return False

    def select_position_by_index(self, index: int = -1):
        """
        Selects a position from the dropdown by index.
        index=0 is first, index=-1 is last.
        """
        self.click(self.position_selector)  # open dropdown

        options = self.page.locator("div.css-1n4zfys")  # update this class as needed
        options.wait_for(state="visible", timeout=10000)

        count = options.count()
        if index < 0:
            index = count + index  # -1 becomes last item
        if index < 0 or index >= count:
            raise IndexError(f"Index {index} is out of range for {count} options.")

        options.nth(index).click()

