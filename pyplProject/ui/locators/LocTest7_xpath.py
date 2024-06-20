from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    #page.locator("xpath=//h1") or page.locator("//h1") --> internally it will detect css or xpath
    page.locator("//h1[@id='navbars']").highlight()
    page.locator("//input[@readonly]").highlight() #attribute