from password import Password


def password_cracker(length, rdn_pass):
    guess = ['a' for i in range(length)]
    print('looking for password...')
    counter = 1

    while not rdn_pass.check_password(''.join(guess)):
        # print(f"checking combination number {counter} ")
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
    print(counter)
    return ''.join(guess)


password_length = 3
rand_pass = Password(password_length)
print(f"password: {rand_pass.password}")
print(f"password found: {password_cracker(password_length, rand_pass)}")
