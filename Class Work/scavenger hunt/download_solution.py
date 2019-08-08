from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(
    "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get(
    "https://www.canadacomputers.com/specials.php?cat=LCD%252FLED+Monitors")

btn_sort = Select(browser.find_element_by_css_selector(
    "select#sort.mx-1.px-0_5.rounded-0.btn-sm.rounded"))
btn_sort.select_by_value('3b')

all_computers = browser.find_elements_by_css_selector(
    "div.productImageSearch.pt-2.pt-sm-0.w-100")

computer_i_want = all_computers[0]
computer_i_want.click()


def find_monitor_size(des):
    inch_index = des.index('"')
    return float(des[inch_index - 3: inch_index])


description = browser.find_element_by_css_selector(
    "h1.h3.product-title.mb-2").text
price = browser.find_element_by_css_selector("span.h2-big").text

print(f'description: {description}')
print(f"monitor size: {find_monitor_size(description)}")
print(f"price: {price}")
