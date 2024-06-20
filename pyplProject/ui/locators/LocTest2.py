from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=900)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    page.get_by_label("Email address").highlight()
    page.get_by_label("Password").highlight()
    page.get_by_label("Example textarea").highlight()
    #to get parent node
    page.get_by_label("Example textarea").locator("..").highlight()