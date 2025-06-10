import pytest
from playwright.sync_api import sync_playwright
from pages.base_page import BasePage  # ✅ reuse timeout logic from BasePage

@pytest.fixture(scope="function")
def page():
    """Provides a configured Playwright page with timeouts from BasePage."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True for now
        context = browser.new_context()
        page = context.new_page()

        # ✅ Apply default timeouts via BasePage
        BasePage(page)

        yield page
        browser.close()
