# Factors of a Number
# Input
import math
start = 1
end = int(input("Enter a value: "))

new_stop = int(math.sqrt(end)) + 1
factor_count = 0
while start < new_stop:
    if end % start == 0:
        dividend = end // start
        if start != dividend:
            factor_count += 2
        else :
            factor_count += 1    
    start += 1
print(f"{end} has {factor_count} factors")