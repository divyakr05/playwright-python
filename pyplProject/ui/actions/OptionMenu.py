from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    dropdown1 = page.get_by_label("Example select")
    dropdown1.select_option("3")
    multiSelect = page.get_by_label("Example multiple select")
    multiSelect.select_option(["2","4"])

    dropdown2 = page.locator("//button[@id='btnGroupDrop1']")
    dropdown2.click()
    dropdownListOption = page.locator("//div[@class='dropdown-menu show']/a[2]")
    dropdownListOption.click()
    browser.close()
