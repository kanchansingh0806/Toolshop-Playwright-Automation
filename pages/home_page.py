class HomePage:

    def __init__(self, page):
        self.page = page
        self.url = "https://practicesoftwaretesting.com/"

    def open(self):
        self.page.goto(self.url)

    def get_page_title(self):
        return self.page.title()

    def click_sign_in(self):
        self.page.get_by_text("Sign in", exact=True).click()

    def search_product(self, product_name):
        self.page.get_by_role("textbox", name="Search").fill(product_name)
        self.page.keyboard.press("Enter")