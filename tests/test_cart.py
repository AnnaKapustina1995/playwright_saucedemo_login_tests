import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@allure.feature("Корзина")
@allure.story("Добавление и удаление товаров")
@allure.title("Добавление и удаление обновляет бейдж и содержимое корзины")
def test_cart_add_and_remove_updates_badge_and_cart_contents(inventory_page: InventoryPage) -> None:
    n: int = 3
    remove_n: int = 1

    added_names = inventory_page.add_first_n_products(n)
    remaining_names = inventory_page.remove_first_n_products(added_names, remove_n)

    inventory_page.open_cart()

    cart_page = CartPage(inventory_page.page)
    cart_page.should_contain_products(remaining_names)
    cart_page.should_not_contain_product(added_names[0])
