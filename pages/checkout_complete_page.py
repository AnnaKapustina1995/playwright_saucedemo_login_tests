from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    PATH: str = "/checkout-complete.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.complete_header: Locator = page.get_by_test_id("complete-header")

    def should_have_success_message(self) -> None:
        expect(self.page).to_have_url(self.url)
        expect(self.complete_header).to_have_text("Thank you for your order!")
