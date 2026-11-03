from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_homepage_loads(page):
    home = HomePage(page)
    home.open()
    assert page.title() != ""
    assert page.locator("body").is_visible()

def test_login_page_navigation(page):
    home = HomePage(page)
    home.open()
    home.click_sign_in()

    assert "login" in page.url.lower()

def test_login(page):
    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_sign_in()

    login.enter_email("kanchan.laksh07@gmail.com")
    login.enter_password("Lovelaksh12!")
    login.click_login()

    assert "account" in page.url.lower()

def test_login_with_invalid_credentials(page):
    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_sign_in()

    login.enter_email("wrong@example.com")
    login.enter_password("WrongPassword123")
    login.click_login()

    assert login.get_error_message() != ""