file = open("stuff.txt")
chinese_nums = [chr(int(x.strip('\n'))) for x in file]
chinese_nums_dict = {str(i): chinese_nums[i] for i in range(11)}

while True:

    chinese_words = list(input())
    answer = [chinese_nums_dict[str(x)] for x in chinese_words]
    print("".join(answer))
