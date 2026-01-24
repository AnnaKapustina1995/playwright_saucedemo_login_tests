from typing import List
from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    PATH: str = "/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_item_names: Locator = page.locator(".cart_item .inventory_item_name")

    def should_contain_products(self, expected_names: List[str]) -> None:

        expect(self.cart_item_names).to_have_count(len(expected_names))

        actual_names: List[str] = [text.strip() for text in self.cart_item_names.all_inner_texts()]

        for name in expected_names:
            assert name in actual_names, (
                f"Товар '{name}' не найден в корзине.\n"
                f"Ожидали: {expected_names}\n"
                f"Фактически: {actual_names}"
            )

    def should_not_contain_product(self, name: str) -> None:
        expect(self.page.get_by_text(name, exact=True)).to_have_count(0)
