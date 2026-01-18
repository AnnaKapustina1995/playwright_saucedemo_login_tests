from playwright.sync_api import expect
from pages.base_page import BasePage
import re


class LoginPage(BasePage):
    url = "https://www.saucedemo.com/"

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR = "[data-test='error']"

    def login(self, username, password):
        self.page.locator(self.USERNAME).fill(username)
        self.page.locator(self.PASSWORD).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()

    def submit_empty(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def should_be_logged_in(self):
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))

    def should_have_error(self, text):
        expect(self.page.locator(self.ERROR)).to_be_visible()
        expect(self.page.locator(self.ERROR)).to_contain_text(text)




