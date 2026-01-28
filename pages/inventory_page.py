from typing import List
import allure
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
        with allure.step("Открыть корзину"):
            self.cart_link.click()

    def should_badge_equal(self, expected: int) -> None:
        with allure.step(f"Проверить бейдж корзины = {expected}"):

            if expected == 0:
                expect(self.cart_badge).to_have_count(0)
            else:
                expect(self.cart_badge).to_have_text(str(expected))

    def add_first_n_products(self, n: int) -> List[str]:
        with allure.step(f"Добавить первые {n} товара(ов) в корзину"):
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

    def remove_product_by_name(self, name: str) -> None:
        with allure.step(f"Удалить товар '{name}' из корзины"):
            item = self.inventory_items.filter(has=self.page.get_by_text(name, exact=True))
            expect(item).to_have_count(1)

            item.get_by_role("button", name="Remove").click()

    def remove_first_n_products(self, names: List[str], n: int) -> List[str]:
        with allure.step(f"Удалить первые {n} товара(ов) из корзины"):
            n = min(n, len(names))

            for i in range(n):
                self.remove_product_by_name(names[i])

            remaining = names[n:]
            self.should_badge_equal(len(remaining))
            return remaining
