from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    emailInput = page.get_by_placeholder("Enter email")
    #fill --> just like copy and paste the text
    emailInput.fill("me@that.site")
    emailInput.clear()
    #type --> just like typing the word, we can add a delay between characters
    emailInput.type("me@that.site",delay=200)
    #input_value() --> to get the value inside input field
    invalid_Input = page.locator("input#inputInvalid").input_value()
    print(invalid_Input)