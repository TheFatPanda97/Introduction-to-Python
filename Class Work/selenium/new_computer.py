from selenium import webdriver

browser = webdriver.Chrome(
    "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get(
    "https://www.bestbuy.ca/en-ca/category/apple-laptops/12746015?sort=priceLowToHigh")
all_computers = browser.find_elements_by_css_selector(
    "div.productPricingContainer_3gTS3")
best_buy_only = browser.find_element_by_css_selector(
    "span.ecomm-webapp-1484.ecomm-webapp-1493.ecomm-webapp-1512.switchLabelText_2Yoro")
best_buy_only.click()

price_comp = {}

for computer in all_computers:
    price = computer.text
    if 'S' in price:
        index_of_s = price.index('S')
        price = float(price[1:index_of_s].replace(',', ''))
    else:
        price = float(price[1:].replace(',', ''))
    price_comp[price] = computer

computer_i_want = price_comp[min(price_comp)]
computer_i_want.click()

txt_description = browser.find_element_by_css_selector("div.description_39c9o")
print(txt_description.text)
