class ProductPage:

    def __init__(self, page):
        self.page = page

    def get_product_results(self):
        return self.page.locator(".card").count()

    def select_first_product(self):
        self.page.locator(".card").first.click()
        self.page.wait_for_url("**/product/**")
        self.page.wait_for_timeout(2000)

    def inspect_product_page(self):
        print("PAGE TITLE:", self.page.title())
        print("PAGE URL:", self.page.url)
        print("BUTTONS:", self.page.locator("button").all_text_contents())
        print("LINKS:", self.page.locator("a").all_text_contents())
        print("PAGE TEXT:", self.page.locator("body").inner_text())