

#input
num = int(input("Enter the nth Fibonacci Number: "))
def fib(num):
    if nth in {0, 1}:
        return nth
    else:
        num1 = 0
        num2 = 1
        num3 = 0
        for i in range(num - 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num3

print(f"Fibonacci Number {num} is {fib(num)}")




