from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_sd_001_login_success(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    login.should_be_logged_in()


def test_sd_002_login_wrong_password(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong_password")
    login.should_have_error("do not match")


def test_sd_003_login_empty_fields(page: Page):
    login = LoginPage(page)
    login.open()
    login.submit_empty()
    login.should_have_error("Username is required")

