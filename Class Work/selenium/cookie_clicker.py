from selenium import webdriver

browser = webdriver.Chrome(
    "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get("https://orteil.dashnet.org/cookieclicker/")

cookie = browser.find_element_by_css_selector("div#bigCookie")
cursor_clicked = False
grandma_clicked = False
farm_clicked = False

while True:
    cookie.click()

    try:
        cursor = browser.find_element_by_css_selector(
            "div#product0.product.unlocked.enabled")
        if not cursor_clicked:
            cursor.click()
            cursor_clicked = True
        cursor_owned = browser.find_element_by_id("productOwned0")
        if int(cursor_owned.text) < 10:
            cursor.click()
    except:
        pass

    try:
        grandma = browser.find_element_by_css_selector(
            "div#product1.product.unlocked.enabled")
        if not grandma_clicked:
            grandma.click()
            grandma_clicked = True
        grandma_owned = browser.find_element_by_id("productOwned1")
        if int(grandma_owned.text) < 5:
            grandma.click()
    except:
        pass

    try:
        farm = browser.find_element_by_css_selector(
            "div#product2.product.unlocked.enabled")
        if not farm_clicked:
            farm.click()
            farm_clicked = True
        farm_owned = browser.find_element_by_id("productOwned2")
        if int(farm_owned.text) < 5:
            farm.click()
    except:
        pass

