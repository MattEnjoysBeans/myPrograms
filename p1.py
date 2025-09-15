# My first program
# Created on 09/15/25
# Purpose: to learn Python
# Editor: Matthew

name = input("Hey there, can I have your name?: ")
age = input("Your Age?: ")

if (int(age) < 13):
    print(f"Hey {name}, you're pretty mature for a {age} year old.")
else:
    print(f"Sorry, {name}, {age}, is too old for me.")
