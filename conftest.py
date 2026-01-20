import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page, playwright):
    playwright.selectors.set_test_id_attribute("data-test")

    login = LoginPage(page)
    login.open()
    return login
