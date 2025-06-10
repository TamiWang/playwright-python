import pytest
from pages.login_page import LoginPage
from pages.dispatch_page import DispatchPage
from pages.initializing_page import InitializingPage

@pytest.mark.smoke
def test_redirects_to_initializing_page(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("tamiw", "admin123")

    dispatch_page = DispatchPage(page)
    dispatch_page.wait_for_position_selector()
   # dispatch_page.select_language_by_text("English - US")
    dispatch_page.click_continue()

    init_page = InitializingPage(page)
    init_page.wait_for_initializing_page()
    assert init_page.is_initializing_displayed()
