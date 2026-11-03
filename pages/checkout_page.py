class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def proceed_to_checkout(self):
        self.page.get_by_role("button", name="Proceed to checkout").click()

    def is_checkout_page_visible(self):
        return "checkout" in self.page.url.lower()