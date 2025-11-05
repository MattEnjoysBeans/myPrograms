#product codes v2

def cleaner(text):
    #text kinda looks like cG23mH-9s
    # WE WANT GH14
    upper_case = ""
    positives = ""
    negatives = ""
    total_sum = 0
    for item in text:
        #print(item)
        if item.isalpha() and item.isupper():
            upper_case += item
            if len(positives) > 0:
                total_sum += int(positives)
                positives = ""
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
        elif item == "-":
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
            else:
                negatives = "-"
        elif item.isdigit():
            if len(negatives) > 0:
                negatives += item
            else:
                positives += item
    #end of for loop

    if len(positives) > 0:
        total_sum += int(positives)

    if len(negatives) > 0:
        total_sum += int(negatives)

    product_code = upper_case + str(total_sum)
    return product_code
    
text = cleaner("cG23mH-9s")
print(text)