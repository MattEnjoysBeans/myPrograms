def isSumLvl1(a_list, target):
    for i in range(len(a_list) - 1):
        for j in range(i + 1, len(a_list)):
            if a_list[j] + a_list[i] == target:
                return True
    return -1

listy = [1,1,2,3,4,5,6,9]
targety = 6
print(isSumLvl1(listy,targety))