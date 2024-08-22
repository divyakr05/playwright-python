from playwright.sync_api import Page  # import Page object from playwright

DOCS_URL = "https://playwright.dev/python/docs/intro"


#def test_verify_url(page): --> page is passing as a fixture. pytest plugin for playwright will handle open a new browser, create a new page etc.

def test_verify_url(page: Page):
    page.goto("https://playwright.dev/python/")
    link = page.get_by_text("Get started")
    link.click()

    assert page.url == DOCS_URL
