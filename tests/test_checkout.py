import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


@allure.feature("Оформление заказа")
@allure.story("Полный сценарий покупки")
@allure.title("Пользователь может оформить заказ до сообщения об успешной покупке")
def test_checkout_flow_finishes_with_success_message(inventory_page: InventoryPage) -> None:
    added_names = inventory_page.add_first_n_products(1)
    inventory_page.open_cart()

    cart_page = CartPage(inventory_page.page)
    cart_page.should_contain_products(added_names)
    cart_page.start_checkout()

    checkout_page = CheckoutPage(inventory_page.page)
    checkout_page.fill_customer_info("Anna", "Kapustina", "12345")
    checkout_page.continue_to_overview()
    checkout_page.finish_checkout()

    checkout_complete_page = CheckoutCompletePage(inventory_page.page)
    checkout_complete_page.should_have_success_message()
