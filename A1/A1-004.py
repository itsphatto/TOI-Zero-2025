try:
    test1 = int(input(""))
    test2 = int(input(""))
    test3 = int(input(""))

    if test1 > 10 or test2 > 40 or test3 > 50:
        print("error1")
    elif test1 > 4 and test2 > 19 and test3 > 24:
        print("pass")
    else:
        print("fail")

except ValueError:
    print("error2")
