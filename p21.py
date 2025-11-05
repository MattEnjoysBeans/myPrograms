def bubble(a_list):
    if not a_list or len(a_list) == 1:
        return a_list
    else:
        didBubble = False
        while not didBubble:   
            for i in range(len(a_list) - 1):
                value1 = a_list[i]
                value2 = a_list[i + 1]
                if value2 < value1:
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    didBubble = True
        return a_list

bigList = [3,1,4,5,6,3,2,1]
newList = bubble(bigList)
print(newList)
            