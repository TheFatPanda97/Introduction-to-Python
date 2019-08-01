# while True:
#     x = input("coordinates\n")
#     if x[0] == "(" and x[-1] == ")" and "," in x:
#         comma_loc = x.index(",")
#         x = x.replace(' ', "")
#         if x[comma_loc - 1].isdigit() and x[comma_loc + 1].isdigit() and len(
#                 x) >= 3:
#             x = x.replace('(', "1", 1)
#             x = x.replace(')', "1", 1)
#             x = x.replace(',', "1", 1)
#             print(x.isdigit())
#         else:
#             print(False)
#     else:
#         print(False)


def create_dict(lst1, lst2):
    new_dict = {}
    for i in range(len(lst1)):
        new_dict[lst1[i]] = lst2[i]
    return new_dict


def convert_to_dict(lst):
    dict = {}
    for i in range(0, len(lst), 2):
        dict[lst[i]] = lst[i + 1]
    return dict

print(convert_to_dict([1,2,3,4]))


l1 = ['a', 'b', 'c']
l2 = [0, 1, 2]

print(create_dict(l1, l2))

d1 = {0: 1, 2: 2}

print(3 in d1)
