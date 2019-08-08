from selenium import webdriver

chrome_driver = "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver"
browser = webdriver.Chrome(chrome_driver)
browser.get(
    "https://classroom.google.com/u/1/c/NDA1MTU2MDYzMzda/a/NDA5OTE2NTEzMjda/details")
btn_add = browser.find_element_by_css_selector("span.GcVcmc.Fxmcue.cd29Sd")
btn_add.click()
