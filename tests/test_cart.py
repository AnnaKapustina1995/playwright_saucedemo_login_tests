from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_badge_and_cart_contains_added_products(inventory_page: InventoryPage) -> None:
    n: int = 3  # можно менять на 1/2/5 — должно работать

    added_names = inventory_page.add_first_n_products(n)
    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.should_contain_products(added_names)
