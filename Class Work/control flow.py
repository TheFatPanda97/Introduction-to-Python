# Evaluates a and b using not and or
def my_add(a, b):
    return not (not a or not b)


def every_2nd(x):
    for i in range(0, len(x), 2):
        print(x[i])


lst = [[1, 2, 3, 4], [1]]


def nested_average(lst):
    num_numbers = 0
    total = 0
    for i in lst:
        for j in i:
            total += j
            num_numbers += 1

    return total / num_numbers


def word_count(x):
    return len(x.split(' '))


def dict_word(x):
    all_words = x.split(" ")
    return {i + 1: all_words[i] for i in range(len(all_words))}


d1 = {0: 'a', 1: 'b', 2: 'c'}
rd1 = {value: key for key, value in d1.items()}
rd1['b'] = 10
d1 = {value: key for key, value in rd1.items()}
print(d1)
