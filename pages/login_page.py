class LoginPage:

    def __init__(self, page):
        self.page = page

    def enter_email(self, email):
        self.page.locator("#email").fill(email)

    def enter_password(self, password):
        self.page.locator("#password").file(password)

    def click_login(self):
        self.page.get_by_role("button",name="Login").click()