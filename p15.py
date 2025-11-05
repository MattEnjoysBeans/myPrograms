def alphaSorting(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(abc)):
        if abc[i] in text.lower():
            result += abc[i]*(text.lower().count(abc[i]))