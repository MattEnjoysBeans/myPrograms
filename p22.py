def inserty(a_list, b_list):
    if len(a_list) in {0, 1}:
        return a_list and b_list
    for i in range(1, len(a_list)):
        j = i
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
                b_list[j-1], b_list[j] = b_list[j], b_list[j-1]
            else:
                break
            j -= 1
    return a_list + b_list

list1 = [3,4,8,6,6,5,5,3,0]
list2 = ['e','r','i','y','y','t','t','e','p']

print(inserty(list1, list2))
    


