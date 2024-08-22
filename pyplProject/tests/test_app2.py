import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


# piece of code in the fixture will be automatically used by every test function, bcz the scope is function by default
@pytest.fixture(autouse=True)
def playwright_page(page: Page):
    page.goto("https://playwright.dev/python/")
    return page


def test_verify_docs_link(page: Page):
    link = page.get_by_role("link", name="Docs")

    assert link.is_visible()


def test_verify_url(page: Page):
    link = page.get_by_text("Get started")
    link.click()

    assert page.url == DOCS_URL
