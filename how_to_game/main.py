from selenium import webdriver

from selenium import webdriver

utorid = "huyingx1"
acorn_password = "ShawnHu0904!"


browser = webdriver.Chrome("C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get("http://www.acorn.utoronto.ca/")
btn_inital_login = browser.find_elements_by_css_selector("a.secondary-btn.secondary-btn-large.btn-secondary")
btn_inital_login[0].click()
txt_username = browser.find_element_by_id("username")
txt_password = browser.find_element_by_id("password")
btn_login = browser.find_element_by_class_name("btn-primary")
txt_username.send_keys(utorid)
txt_password.send_keys(acorn_password)
btn_login.click()
browser.get("https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/courses/0")
all_courses = browser.find_elements_by_css_selector("div.currentlyEnrolledBox.courseSearchBox.disabled")
print(all_courses)

