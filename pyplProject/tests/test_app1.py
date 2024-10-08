import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture
def playwright_page(page: Page):
    page.goto("https://playwright.dev/python/")
    return page


def test_verify_docs_link(playwright_page: Page):
    link = playwright_page.get_by_role("link", name="Docs")

    assert link.is_visible()


def test_verify_url(playwright_page: Page):
    link = playwright_page.get_by_text("Get started")
    link.click()

    assert playwright_page.url == DOCS_URL
