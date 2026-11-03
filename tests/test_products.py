from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage


def test_search_product(page):
    home = HomePage(page)
    product = ProductPage(page)

    home.open()
    home.search_product("Hammer")

    assert product.get_product_results() > 0

def test_add_product_to_cart(page):
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    home.open()
    home.search_product("Hammer")
    product.select_first_product()
    product.inspect_product_page()
    cart.add_to_cart()
    cart.open_cart()

    assert "Product added to shopping cart." in cart.get_cart_text()

def test_proceed_to_checkout(page):
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    home.open()
    home.search_product("Hammer")
    product.select_first_product()
    cart.add_to_cart()
    cart.open_cart()
    checkout.proceed_to_checkout()

    assert checkout.is_checkout_page_visible()