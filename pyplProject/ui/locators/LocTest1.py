from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    chkbox = page.get_by_role('checkbox',name="Default checkbox")
    chkbox.highlight()
    chkbox.check()
    page.get_by_role('button',name='Primary').locator("nth=2").highlight()
    page.get_by_role("heading").filter(has_text="Heading").highlight()
