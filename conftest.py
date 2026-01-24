import pytest
from playwright.sync_api import Page, Playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def login_page(page, playwright):
    playwright.selectors.set_test_id_attribute("data-test")

    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def inventory_page(login_page: LoginPage) -> InventoryPage:
    login_page.login("standard_user", "secret_sauce")
    login_page.should_be_logged_in()
    return InventoryPage(login_page.page)
