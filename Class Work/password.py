from random import randint


class Password:

    def __init__(self, length):
        password = ''
        for i in range(length):
            num = randint(0, 1)
            if num:
                random_letter = chr(randint(48, 57))
            else:
                random_letter = chr(randint(97, 122))
            password += random_letter

        if password.isdigit():
            random_index = password[randint(0, len(password) - 1)]
            random_letter = chr(randint(97, 122))
            password = password.replace(random_index, random_letter, 1)
        elif password.isalpha():
            random_index = password[randint(0, len(password) - 1)]
            random_letter = chr(randint(48, 57))
            password = password.replace(random_index, random_letter, 1)
        self.password = password

    def check_password(self, password):
        return self.password == password
