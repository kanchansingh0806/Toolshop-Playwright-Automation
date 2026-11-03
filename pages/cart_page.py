class CartPage:

    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.page.get_by_role("link", name="Cart").click()

    def get_cart_text(self):
        return self.page.locator("body").inner_text()

