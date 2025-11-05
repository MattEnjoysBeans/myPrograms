def isPalindrome(word):
    return word == word[::-1]

text = input("Enter a word: ")
if isPalindrome(text):
    print(f"{text} is a palindrome")
else:
    print(f"{text} is boring")