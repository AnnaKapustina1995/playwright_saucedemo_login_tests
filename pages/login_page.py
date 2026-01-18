from playwright.sync_api import expect
from pages.base_page import BasePage
import re


class LoginPage(BasePage):
    path = "/"

    def username_input(self):
        return self.page.get_by_placeholder("Username")

    def password_input(self):
        return self.page.get_by_placeholder("Password")

    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    def error_block(self):
        return self.page.locator("[data-test='error']")

    def login(self, username: str, password: str):
        self.username_input().fill(username)
        self.password_input().fill(password)
        self.login_button().click()

    def submit_empty(self):
        self.login_button().click()

    def should_be_logged_in(self):
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))

    def should_have_error(self, text: str):
        expect(self.error_block()).to_be_visible()
        expect(self.error_block()).to_contain_text(text)





