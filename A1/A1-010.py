try:
    age = int(input(""))
    status = input("")[0]

    if age < 18 or status.lower() == 's':
        print("20")
    else:
        print("50")

except ValueError:
    print("valueerror")
