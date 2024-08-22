import pytest
from playwright.sync_api import TimeoutError, Page, expect


def test_hidden_layer(page: Page):
    page.goto("http://www.uitestingplayground.com/hiddenlayers")
    grn_btn = page.locator("button#greenButton")
    grn_btn.click()

    with pytest.raises(TimeoutError):
        grn_btn.click(timeout=2000) # playwright won't attempt to click a hidden element, this piece of code will raise the error, wait for 2 sec, playwright catches the error
