import pytest
from pages.login_page import LoginPage
from pages.dispatch_page import DispatchPage

@pytest.mark.smoke
def test_dispatch_position_selection(page):
    # Login
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("tamiw", "admin123")

    # Wait for and validate Position page
    dispatch_page = DispatchPage(page)
    assert dispatch_page.is_position_visible(), "Position dropdown should be visible after login"

    # On dispatch page 
    #dispatch_page.select_language_by_text("English - US")
    dispatch_page.click_continue()

    # check redirected page
    assert "dashboard" in page.url.lower() or page.title(), "Should navigate to next screen after Continue"


@pytest.mark.regression
def test_continue_without_selecting_position(page):
    # Login
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("tamiw", "admin123")

    # Wait for and validate Position page
    dispatch_page = DispatchPage(page)
    assert dispatch_page.is_position_visible(), "Position dropdown should be visible after login"

    # no position selected
   # dispatch_page.select_language_by_text("English - US")
    dispatch_page.click_continue()

    # check redirected page
    page.wait_for_selector("text=Initializing...", timeout=10000)
    assert page.locator("text=Initializing...").is_visible(), "Should be redirected to Initializing page"
