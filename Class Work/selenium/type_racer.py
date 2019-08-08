from selenium import webdriver
import time

username = 'imapp'
password = 'Alien!'

browser = webdriver.Chrome(
    "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get(
    "https://play.typeracer.com/")
time.sleep(0.5)

all = browser.find_elements_by_css_selector("a.gwt-Anchor")
practice = ''
btn_sign = all[0]
btn_sign.click()
txtf_username = browser.find_element_by_css_selector("input.gwt-TextBox")
txtf_password = browser.find_element_by_css_selector(
    "input.gwt-PasswordTextBox")
btn_login = browser.find_element_by_css_selector("button.gwt-Button")

txtf_username.send_keys(username)
txtf_password.send_keys(password)
btn_login.click()

time.sleep(3)
print(all)

for x in all:
    # print(x.text)
    if x.text == 'Practice':
        x.click()
        break


txt_message = browser.find_elements_by_css_selector("span")
print(txt_message[5].text)
print(txt_message[6].text)
print(txt_message[7].text)

message = txt_message[6].text + txt_message[7].text + ' ' + txt_message[
    8].text + ' '
print(message)

txt_bar = browser.find_element_by_css_selector("input.txtInput")

time.sleep(9)

txt_bar.click()
txt_bar.send_keys(message)

# for letter in message:
#     txt_bar.send_keys(letter)
    # time.sleep(0.085)
