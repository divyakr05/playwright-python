import pytest
import re
from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"
DOCS_TITLE = "Installation | Playwright Python"


def test_get_started_link(page: Page):
    '''
    page.goto("https://playwright.dev/python")

    # link = page.get_by_role("link", name="GET STARTED")
    # link.click()

    # page assertions
    # expect(page).to_have_url(DOCS_URL)
    # expect(page).to_have_url("Get Python")
    # expect(page).to_have_title(DOCS_TITLE)

    # Element state assertions
    # expect(link).not_to_be_visible()
    # expect(link).to_be_hidden()

    # Inner text assertions
    # heading = page.locator("//h1[contains(@class,'hero__title hero')]")
    # expect(heading).to_contain_text("end-to-end testing")
    # dropdown = page.locator("//ul[contains(@class,'dropdown')]")
    # expect(dropdown).to_contain_text("Python")
    # expect(dropdown).to_contain_text("Node.js")
    # expect(dropdown).to_contain_text("Java")
    # expect(dropdown).to_contain_text(".NET")

    # Attribute assertions
     docs_link = page.get_by_role("link", name="Docs")
     expect(docs_link).to_have_class("navbar__item navbar__link")
     regular expression to check the class that starts with
     expect(docs_link).to_have_class(
        re.compile(r"^navbar__item")
    )
    expect(docs_link).to_have_attribute(
        "href", "/python/docs/intro"
    )


    # Input field assertions
    search_btn = page.locator("//span[text()='Search']")
    input_searchDocs = page.get_by_placeholder("Search docs")
    # input is hidden before button click
    expect(input_searchDocs).to_be_hidden()
    search_btn.click()
    expect(input_searchDocs).to_be_editable()
    expect(input_searchDocs).to_be_empty()

    # type some query in the input
    query = "assertions"
    input_searchDocs.fill(query)

    # check input value
    expect(input_searchDocs).to_have_value(query) '''

    # Checkbox Assertions
    page.goto("https://bootswatch.com/default")
    checked_checkbox = page.get_by_label("Checked checkbox")
    default_checkbox = page.get_by_label("Default checkbox")

    expect(checked_checkbox).to_be_checked()
    expect(default_checkbox).not_to_be_checked()

    # Option Menu Assertions
    option_menu = page.get_by_label("Example select")
    expect(option_menu).to_have_value("1")
    multi_option_menu = page.get_by_label("Example multiple select")
    expect(multi_option_menu).to_have_values([])
    multi_option_menu.select_option(["2", "4"])
    expect(multi_option_menu).to_have_values(["2", "4"])