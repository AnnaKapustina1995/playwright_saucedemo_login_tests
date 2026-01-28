import re
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error = page.get_by_test_id("error")

    def login(self, username: str, password: str):
        with allure.step(f"Ввести логин '{username}' и пароль, нажать Login"):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()

    def should_be_logged_in(self):
        with allure.step("Проверить, что пользователь успешно вошёл и открыт inventory"):
            expect(self.page).to_have_url(re.compile(r".*/inventory\.html$"))

    def should_have_error(self, text: str):
        with allure.step(f"Проверить, что показана ошибка и содержит текст: '{text}'"):
            error = self.error
            expect(error).to_be_visible()
            expect(error).to_contain_text(text)
