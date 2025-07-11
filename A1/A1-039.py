def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        print("Put Positive Integer only")
    else:
        k = 1
        for i in range(2, n + 1):
            k *= i
        return k

try:
    number = int(input(''))
    result = factorial(number)
    if result is not None:
        print(f"{result}")
except ValueError:
    print("Positive Integer only")
