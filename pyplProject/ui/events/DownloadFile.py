from playwright.sync_api import sync_playwright

def on_download(download):
    print("Download received")
    download.save_as("newText1.txt")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=700
    )
    # download using with context manager
    '''page = browser.new_page()
    page.goto("https://commitquality.com/practice-file-download")
    btn = page.get_by_text("Download File")

    with page.expect_download() as download_info:
        btn.click()
    download = download_info.value
    download.save_as("newText.txt")'''

    # another way using event listener
    page = browser.new_page()
    page.goto("https://commitquality.com/practice-file-download")
    page.on("download", on_download)
    btn = page.get_by_text("Download File")

    with page.expect_download() as download_info:
        btn.click()

    browser.close()
