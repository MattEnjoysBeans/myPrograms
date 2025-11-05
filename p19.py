#empty list
a_list = []
#determine if a list is empty
if not a_list:
    print("a_list is empty!")
# what does len(), sum(), min(), max() do
c_list = [3,1,4,1,5,9]
print(len(c_list)) # expect 6
print(sum(c_list)) # expect 23
print(min(c_list)) # expect 1
print(max(c_list)) # expect 9
#access individual items in a list
d_list = list("hello, world!")
print(d_list[0]) # "h"
print(d_list[-1]) # "!"
print(d_list[1:4]) # ["e", "l", "l"]
#join two/multiple lists together
a = [3,1,4]
b = ["Marshall", "Freya", "Joy"]
c = a + b # creates a new list of a and b joined
a.extend(b) # mutates to give the contents of b
a = [3,1,4]
for item in b:
    a.append(item)