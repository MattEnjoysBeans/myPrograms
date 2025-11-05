def linSearch(text, target):
    if not text:
        return -1
    else:
        for i in range(len(text)):
            if text[i] in target:
                return i

        return -1


print("Jasper... where is p?", linSearch("Jasper", "p"))