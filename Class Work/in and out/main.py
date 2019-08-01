while True:
    sentence = input().split(" ")
    encrypted = []

    for word in sentence:
        new_word = ''
        for letter in word:
            if ord(letter) >= 120:
                new_word += chr(ord(letter) - 23)
        encrypted.append(new_word)

    print(" ".join(encrypted))
