from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browse = p.chromium.launch(headless=False)
    page = browse.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    print(page.title())
    browse.close()