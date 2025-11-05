example = [2,3,3,6,5,9,10,100,14,17]

def mean(a_list):
    sum = 0
    for i in a_list:
        sum += i
    return sum / len(a_list)

def bubble(a_list):
    isSwapped = True
    while isSwapped:
        isSwapped = False
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                isSwapped = True

def median(a_list):
    a_list = bubble(a_list)
    if len(a_list) % 2 == 0:
        median = (a_list[(len(a_list) - 1) // 2] + a_list[(len(a_list) - 1) // 2 + 1]) / 2
        return median
    else:
        return a_list[(len(a_list) - 1) // 2]


print(median(example))