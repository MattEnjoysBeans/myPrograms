# Donut Shop Problem
# input
donutCount = int(input("How many donuts are available in the shop: "))
events = int(input("Enter the number of events: "))

# We stop when no donuts left or no events
currentEvent = 1
while current_event <= to events and donutCount >= 0:
    eventType = input("+ or -?: ")
    donutAmount = int(input("Enter donut amount: "))
    if eventType == "+":
        donutCount += donutAmount
    elif event_type == "-":
        donutCount -= donutAmount
    else:
        print("Invalid Option")

    # end of loop
    print(f"At the end of our events, we have {donutCount} donuts.")