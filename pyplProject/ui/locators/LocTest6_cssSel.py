from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    #locating 4 types of css sel: tagname, class, id and attribute
    #either css=h1 or h1 is fine
    #page.locator("css=h1").highlight()
    #page.locator("footer").highlight()
    #to locate with class using css selector --> tagname.classname
    #page.locator("button.btn-success").highlight()
    # to locate with id using css selector --> tagname#id
    page.locator("button#btnGroupDrop1").highlight()
    # to locate with an attribute using css selector --> tagname[attribute]
    page.locator("input[readonly]").highlight()
    # to locate with an attribute and its value using css selector --> tagname[attribute]
    page.locator("input[value = 'correct value']").highlight()
    # to locate with multiple values using css selector --> tagname.class#id
    page.locator("a.nav-link#themes").highlight()

    #parent child using css sel --> parent child
    page.locator("nav.bg-dark a.active").highlight()
    # to locate child directly under parent (direct child)--> parent > child
    page.locator("nav.bg-dark a.active").highlight()
    #if there are multiple childs directly under parent, to select first --> parent > :first-child
    page.locator("div.bs-component >:first-child ul.list-group").highlight()


    #css selectors - pseudo classes
    page.locator("h1:text-is('Navs')").highlight()
    #n-th match element
    page.locator(":nth-match(button.btn-primary,4)").highlight()
    page.locator(":nth-match(div.bs-component > ul.list-group,1)").highlight()
    page.locator(":nth-match(button:text('Primary'),4)").highlight()