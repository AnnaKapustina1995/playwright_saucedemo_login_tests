from typing import List
from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PATH: str = "/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_link: Locator = page.get_by_test_id("shopping-cart-link")
        self.cart_badge: Locator = page.get_by_test_id("shopping-cart-badge")
        self.inventory_items: Locator = page.locator(".inventory_item")

    def open_cart(self) -> None:
        self.cart_link.click()

    def should_badge_equal(self, expected: int) -> None:
        if expected == 0:
            expect(self.cart_badge).to_have_count(0)
        else:
            expect(self.cart_badge).to_have_text(str(expected))

    def add_first_n_products(self, n: int) -> List[str]:
        count: int = self.inventory_items.count()
        n = min(n, count)

        added_names: List[str] = []

        for i in range(n):
            item = self.inventory_items.nth(i)

            name = item.locator("[data-test='inventory-item-name']").inner_text().strip()
            item.get_by_role("button", name="Add to cart").click()

            added_names.append(name)

        self.should_badge_equal(n)
        return added_names
