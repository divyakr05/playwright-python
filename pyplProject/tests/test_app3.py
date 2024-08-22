import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


# piece of code in the fixture will be automatically used by every test function, bcz the scope is function by default
@pytest.fixture(autouse=True, scope="function")
def playwright_page(page: Page):
    page.goto("https://playwright.dev/python/")
    # yield --> we can run some code and pass an object back to the requesting fixture/test
    # before test function
    yield page
    # after test function
    page.close()
    print("\n [ Fixture ]: page closed!")


def test_verify_docs_link(page: Page):
    link = page.get_by_role("link", name="Docs")
    page.screenshot(path="playwright.jpg")
    assert link.is_visible()


def test_verify_url(page: Page):
    link = page.get_by_text("Get started")
    link.screenshot(path="link.jpg")
    link.click()
    assert page.url == DOCS_URL
