def isPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        divider = 3
        upper_limit = int(num**0.5) + 1
        while divider < max(upper_limit, 3):
            if num % divider == 0:
                return False
            divider += 2
        return True

for i in range(0, 1000000):
    if isPrime(i):
        print(i)
            
