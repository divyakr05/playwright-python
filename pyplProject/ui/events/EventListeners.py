from playwright.sync_api import sync_playwright
from time import perf_counter

def on_load(page):  #here the event is a page object
    print("Page loaded:", page)

def on_request(request):
    print("Request sent:", request)

def on_filechooser(file_chooser):
    print("File chooser opened:")
    file_chooser.set_files("C:/Users/divyar/PycharmProjects/pyplProject/.venv/image.jpg")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    page = browser.new_page()
    # page.on("load",on_load) # this is the event listener --> if the event(load) happens, then on_load method is called
    # page.once("load",on_load) # if you want listen to the event once
    # similarly we can listen to other events
    # page.on("domcontentloaded", on_domcontentloaded)
    # page.on("close", on_close) # whenever the page gets closed
    # page.on("request", on_request) # whenever a request is sent for a html,css,js,img,svg etc. files
    # page.on("response", on_response) # whenever a response is sent
    page.on("filechooser", on_filechooser)
    # !!!!!!!!!!!!! MAKE SURE YOU REGISTER THE LISTENER BEFORE THE ACTION !!!!!!!!!!!!!
    page.goto("https://bootswatch.com/default")
    file_input = page.locator("//input[@type='file']")
    file_input.click() # whenever you click on file chooser, method is called

    # Remove the listener if you want to terminate
    page.remove_listener("load",on_load())
    browser.close()
