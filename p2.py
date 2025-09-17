# Rollecoaster ride program
# input
place_in_Line = int(input("What place in line are you?: "))
cartNum = int(input("How many cars does the train have?: "))
cartMax = int(input("What is the maximum number of people carriable in a car?: "))

# procesing 
if cartNum * cartMax >= place_in_Line:
    print("yes")
else:
    print("no")