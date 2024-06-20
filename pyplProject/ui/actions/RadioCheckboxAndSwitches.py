from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    radio = page.get_by_label("Option two can be something else and selecting it will deselect option one")
    radio.check() # check --> only check if unchecked, otherwise it will be skipped
    print(radio.is_checked())
    checkbox = page.get_by_label("Default checkbox")
    checkbox.check()
    print(checkbox.is_checked())
    checkbox.click()
    switch = page.get_by_label("Default switch checkbox input")
    switch.check()
    switch.click()
    switch.check()
    switch.uncheck()
    switch.set_checked(True)
    switch.set_checked(False)
