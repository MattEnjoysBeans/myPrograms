def clean(text):
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
        result = result + text[i].lower()
    return result

word = input("Enter a string: ")
print(f"The cleaned up text is: {clean(word)}")

