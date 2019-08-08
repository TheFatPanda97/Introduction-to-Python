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


# TODO 1 choose the correct computer to click on from the list all_computers
################################################################################


################################################################################


# TODO 2 finis this function!
def find_monitor_size(description):
    pass

# TODO 3 find and print the description, monitor size, and price
################################################################################


################################################################################
