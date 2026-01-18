from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://www.saucedemo.com"
    path = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(f"{self.BASE_URL}{self.path}")


