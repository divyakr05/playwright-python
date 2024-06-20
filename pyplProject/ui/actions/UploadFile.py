from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    ''' browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    file_input = page.locator("//input[@type='file']")
    file_input.set_input_files("C:/Users/divyar/PycharmProjects/pyplProject/.venv/textFile.txt")
    browser.close() '''


    #upload from file chooser
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    page = browser.new_page()
    page.goto( "https://commitquality.com/practice-file-upload")
    file_input = page.locator("//input[@type='file']")
    #using page objects,ie. playwright's expect_file_chooser()
    #store the file chooser in fc_info and do the action(click) that triggers upload
    with page.expect_file_chooser() as fc_info:
        file_input.click()
    file_chooser = fc_info.value
    file_chooser.set_files("C:/Users/divyar/PycharmProjects/pyplProject/.venv/image.jpg")




