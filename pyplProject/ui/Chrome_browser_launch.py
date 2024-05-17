from playwright.sync_api import sync_playwright

#start a new playwright instance
#playwright = sync_playwright().start()

#with context manager to start and close the instance
with sync_playwright() as playwright:
    #launch browser
    #browser = playwright.chromium.launch() --> headless mode, cannot see the ui, headless=True by default
    browser = playwright.chromium.launch(headless=False, slow_mo=500) # slow_mo --> slows down the exec speed by 500 times(500 milli sec)
    #create a new page
    page = browser.new_page()
    #load url
    page.goto("https://playwright.dev/python")
    browser.close()


'''def demo():
    print("hello world")

def test_demo():
    demo()

def test_demo1():
    print("myeas")'''