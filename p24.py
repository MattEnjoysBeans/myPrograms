def find(target, a_list):
    if target < a_list[0] or target > a_list[-1]:
        return False
    else:
        b_list = a_list
        while True:
            if target == b_list[len(b_list) // 2]:
                return b_list[len(b_list) // 2]
            elif target == b_list[len(b_list) // 2 + 1]:
                return b_list[len(b_list) // 2 + 1]
            elif target < b_list[len(b_list) // 2 + 1]:
                b_list = b_list[0:len(b_list) // 2]
            else:
                b_list = b_list[len(b_list) // 2:-2]

listy = []
listy.extend(range(10000000))
targety = 758
print(find(targety,listy))
