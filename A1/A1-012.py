try:
    number = int(input(""))
    reversenumber = int(str(number)[::-1])
    operator = input("")

    if operator == '+':
        result = number + reversenumber
        print(f"{number} + {reversenumber} = {result}")
    elif operator == '*':
        result = number * reversenumber
        print(f"{number} * {reversenumber} = {result}")
    else:
        print("error put + or *")

except ValueError:
    print("value error")
