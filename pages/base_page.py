from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://www.saucedemo.com"
    PATH: str  # только type (обязаны определить в наследнике)

    def __init__(self, page: Page):
        if not hasattr(self.__class__, "PATH"):
            raise NotImplementedError(f"{self.__class__.__name__} must define PATH")
        self.page = page
        self.url = f"{self.BASE_URL}{self.PATH}"

    def open(self):
        self.page.goto(self.url)
