from playwright.sync_api import sync_playwright


def on_dialog_confirmation(dialog):
    print("Dialog opened:", dialog)
    dialog.accept()
    # dialog.dismiss()


def on_dialog_prompt(dialog):
    print("Dialog opened:", dialog)
    dialog.accept("Playwright is cool !!!")
    # dialog.dismiss()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=700
    )
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    # simple alert --> playwright will handle it automatically
    # btn1 = page.get_by_text("Click for JS Alert")
    # btn1.click()

    # confirmation alert
    '''page.on("dialog", on_dialog_confirmation)
    btn2 = page.get_by_text("Click for JS Confirm")
    btn2.click()  # here calls the method on_dialog '''

    # confirmation alert
    page.on("dialog", on_dialog_prompt)
    btn3 = page.get_by_text("Click for JS Prompt")
    btn3.click()  # here calls the method on_dialog
    browser.close()
