from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    # Generic click
    button = page.get_by_role("button",name="Block button").first
    button.click()

    # Double click
    button.dblclick()
    # Double click with a delay of 500ms
    button.dblclick(delay=500)

    # Right click
    button.click(button="right")

    # click on element after pressing multiple keys
    button.click(modifiers = ["Shift"])
    button.click(modifiers = ["Shift", "Control"])

    # Hover over element
    button1 = page.locator("button.btn-outline-primary")
    button1.hover()

