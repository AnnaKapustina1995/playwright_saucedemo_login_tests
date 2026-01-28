from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    PATH: str = "/checkout-step-one.html"

    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name: Locator = page.get_by_placeholder("First Name")
        self.last_name: Locator = page.get_by_placeholder("Last Name")
        self.postal_code: Locator = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button: Locator = page.get_by_role("button", name="Continue")
        self.finish_button: Locator = page.get_by_role("button", name="Finish")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_to_overview(self) -> None:
        self.continue_button.click()
        expect(self.page).to_have_url(self.BASE_URL + "/checkout-step-two.html")

    def finish_checkout(self) -> None:
        self.finish_button.click()
