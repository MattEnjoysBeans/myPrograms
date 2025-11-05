listA = ["cG23mH-9s"]
#negatives will have the - symbol at that index minus 1
#add all digits to one string
#add all alphas to another

for i in listA:
    newLetters = ""
    newNumsStr = ""
    newNums
    newCode = ""
    for item in i:
        if item.isupper() and item.isalpha():
            newLetters += item
        elif item.isdigit:
            if i[item.find(item)-1] == "-":
                newNums = "-" + item
            else:
                newNums += item
    
newCode = newLetters + newNums
print(newCode)