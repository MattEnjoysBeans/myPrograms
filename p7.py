num = 6

def perfectNum(num):
    start = 1
    perfectCount = 0
    while start < num:
        if num % start == 0:
            perfectCount += start
        start += 1
    return perfectCount == num

while num < 100000:
    if perfectNum(num):
        print(f"{num} is perfect")
    num += 2

    
