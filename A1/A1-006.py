try:
    a = int(input(""))
    b = int(input(""))

    if b == 0:
        print("math error")
    elif a % b == 0:
        print("yes")
    else:
        print("no")

except ValueError:
    print("value error")