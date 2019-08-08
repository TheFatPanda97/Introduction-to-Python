from random_password import check_password
from selenium import webdriver


def password_cracker(length):
    guess = ['a' for i in range(length)]
    print('looking for password...')
    counter = 1

    while not check_password(''.join(guess)):
        counter += 1

        if guess[0] == '9':
            guess[0] = 'a'
            guess[1] = chr(ord(guess[1]) + 1)
        elif guess[0] == 'z':
            guess[0] = '0'
        else:
            guess[0] = chr(ord(guess[0]) + 1)

        for i in range(1, len(guess)):
            if guess[i] == ':':
                guess[i] = 'a'
                if i != len(guess) - 1:
                    guess[i + 1] = chr(ord(guess[i + 1]) + 1)
            elif guess[i] == 'z':
                guess[i] = '0'
    print(f"password found: {''.join(guess)}")
    return ''.join(guess)


password_length = 4
browser = webdriver.Chrome(
    "C:\\Users\\husha\\Downloads\\chromedriver_win32\\chromedriver")
browser.get("https://pastebin.com/login")
username = 'IMAPP'
password = password_cracker(password_length)

inputs = browser.find_elements_by_css_selector("input.post_input.width_390")
btn_login = browser.find_element_by_css_selector("input.button1.btnbig")
txtf_username = inputs[0]
txtf_password = inputs[1]

txtf_username.send_keys(username)
txtf_password.send_keys(password)
btn_login.click()
