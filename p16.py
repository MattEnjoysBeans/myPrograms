#string checklist
#empty string
stringEmpty = ""
#determine if a string is empty
if not stringEmpty:
    print("burga")
#format a string to contain dynamic data
name = "skibidiah"
strVar = f"Hello {name}!"
#access individual chars/items in a string
print(name[0])
#Access the first, access the last item in a string
print(name[0])
print(name[-1])
#join two/multiple strings together
print(name + "burga")
#reverse a string
print(name[::-1])
v2 = ''.join(reversed(name))
print(v2)
#create a copy of a string
temp = "hydroflask"
temp_copy = temp[:]
#compare strings for equality
a = "marshall"
b = "dog"
status = a == b
#determine the min and max value within a string
print(max(temp))
print(min(temp))
print(max('hello', 'goodbye'))
print(min('1', '2', '3', '!'))
# determine if an item/patter exists within a string
word = "poopooplatter"
if "poo" in word:
    print("THERE IS POO!")
# determine the index of an item or patter within a string
poopLocation = word.find("poo")
poopLocation = word.index("poop")
#Count how often an item or a pattern occurs within a string
poopCount = word.count("poo")
#convert all items in a string to uppercase/lowercase
yellHydroflask = temp.upper()
quietHydroflask = yellHydroflask.lower()
#determine if a string can be converted to an integer
# convert a string to an integer
strNum = "67"
num = 0
if strNum.isdigit(): #checks if only digits
    num = int(strNum)
#determine if a string only contains alphabetical char
word = "shsm".isalpha()
#remove nonalpha characters from a string
# sometimes its easier to create rather than destroy
gibberish = "sakdj1209dj10909j1309jd910j90"
clean = ""
for i in range len(gibberish):
    #finding all special characters too
    if not gibberish[i].isalpha():
        clean += gibberish[i]
# Remove all whitespaces from a string
example = " h h h h h  h h h h  h h  h"
example = example.replace(" ", "")
# sort a string in ASCII order or reverse-ASCII order