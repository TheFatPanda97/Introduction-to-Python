from selenium import webdriver

browser = webdriver.Chrome(
    "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get("https://pastebin.com/login")
username = 'IMAPP'
password = 'dp91'

inputs = browser.find_elements_by_css_selector("input.post_input.width_390")
btn_login = browser.find_element_by_css_selector("input.button1.btnbig")
txtf_username = inputs[0]
txtf_password = inputs[1]

txtf_username.send_keys(username)
txtf_password.send_keys(password)
btn_login.click()
