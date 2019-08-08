from selenium import webdriver

browser = webdriver.Chrome(
    "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get("https://www.theweathernetwork.com/ca/weather/ontario/mississauga")

search_bar = browser.find_element_by_id("search")
search_bar.send_keys("beijing")
search_bar.send_keys("\ue007")

all_buttons = browser.find_elements_by_css_selector("li.result")

# for x in all_buttons:
#     print(x.text)

all_buttons[0].click()
txt_temperature = browser.find_element_by_css_selector("p.mcity-feels-like")
print(txt_temperature.text)

