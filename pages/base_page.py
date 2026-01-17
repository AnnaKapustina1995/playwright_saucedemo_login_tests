from playwright.sync_api import Page


class BasePage:
    url = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if not self.url:
            raise ValueError("url is not set for this page")
        self.page.goto(self.url)

