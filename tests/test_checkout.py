from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_checkout_flow_finishes_with_success_message(inventory_page: InventoryPage) -> None:
    added_names = inventory_page.add_first_n_products(1)
    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.should_contain_products(added_names)
    cart.start_checkout()

    checkout = CheckoutPage(inventory_page.page)
    checkout.fill_customer_info("Anna", "Kapustina", "12345")
    checkout.continue_to_overview()
    checkout.finish_checkout()

    complete = CheckoutCompletePage(inventory_page.page)
    complete.should_have_success_message()
