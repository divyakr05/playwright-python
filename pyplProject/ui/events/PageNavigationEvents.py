from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=700
    )
    page = browser.new_page()
    print("Page loading...")
    start = perf_counter()
    page.goto(
        "https://playwright.dev/python/",
        # https://playwright.dev/python/docs/api/class-page
        wait_until='load'   # with load event, we wait for all the resources in the web page to load in(images, icons, etc.)
                            # this is configured by default in goto navigation method

        #wait_until ='domcontentloaded' # wait for all the dom contents --> HTML document(lesser time than load event)
        # does not wait for the resources like images, icons etc.

        # wait_until ='commit' # it waits for the html response from the server and gets called this(lesser time than domcontentloaded event)
        # does not wait for html to parse and display in the browser

        # wait_until ='networkidle' # it waits for all the network events to happen in our browser(more time than load event)

              )
    time_taken = perf_counter()-start
    print(f"...Page loaded in {round(time_taken, 2)}seconds") #round it to 2 decimal places

    browser.close()
