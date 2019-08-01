# x = [i for i in range(1, 11)]


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
# def magic(lst):
#     num = lst[0]
#     for i in range(0, 10, 4):
#         num += lst[i]
#     return num
#
#
# print(magic(x))


# def count_a(x):
#     count = 0
#     num_a = 0
#     while count < len(x):
#         if x[count] == 'a':
#             num_a += 1
#         count += 1
#     return num_a


x = [1, 2, 3]
y = [4, 5, 1, 2, 4, 1]


def combine(lst1, lst2):
    final = []
    for i in lst1:
        final.append(i)
    for j in lst2:
        final.append(j)
    return final


print(combine(x, y))

x = 99
print(x % 2/0)
