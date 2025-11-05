def select(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        i = 0
        while i < len(a_list):
            smallest = a_list[i] # then prove it is or isnt
            # start hunt
            j = i + 1
            new_location = i
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest:
                    smallest = new_value
                    new_location = j
                j += 1
            # end of hunt
            # swap the smallest into the proper location
            temp = a_list[i]
            a_list[i] = smallest
            a_list[new_location] = temp
            # python way
            a_list[i], a_list[new_location] = a_list[new_location], a_list[i]
            i += 1

