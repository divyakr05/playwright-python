from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    textarea = page.get_by_label("Example textarea")
    textarea.press("KeyW") #lower case
    textarea.press("KeyO")
    textarea.press("KeyR")
    textarea.press("Shift+KeyD") #upper case

    textarea.press("Control+ArrowLeft") #cursor move to the starting position
    textarea.press("ArrowRight") #cursor move to the right by one