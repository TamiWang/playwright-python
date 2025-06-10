import pytest
from pages.login_page import LoginPage
from pages.dispatch_page import DispatchPage

@pytest.mark.smoke
def test_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("tamiw", "admin123")

    dispatch_page = DispatchPage(page)
    assert dispatch_page.is_position_visible()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("wronguser", "wrongpass")

    login_page.wait_until_visible("span.error-msg")
    assert login_page.is_error_displayed()
    assert "invalid" in login_page.get_error_message().lower()
