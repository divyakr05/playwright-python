from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    #page.get_by_text("with faded secondary text").highlight()
    page.get_by_text("Small button").highlight()

