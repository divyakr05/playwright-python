from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=700
    )
    page = browser.new_page()
    print("Page loading...")
    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")
    link = page.get_by_role('link', name="2015")
    link.click()
    start = perf_counter()
    tableDataFirst = page.locator("//tr[@class='film']/td").first
    # https://playwright.dev/docs/actionability
    tableDataFirst.wait_for(timeout=1000) # default wait time is 30 sec. Here, reduced the timeout to 1 sec and try
    time_taken = perf_counter()-start
    print(f"...Page loaded in {round(time_taken, 2)}s") #round it to 2 decimal places

    browser.close()
