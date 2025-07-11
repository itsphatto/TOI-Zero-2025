def get_season(month, day):
    if month not in range(1, 13) or day not in range(1, 32):
        return "error date"
    if (month == 3 and day >= 21):
        season = "spring"
    elif (month == 6 and day >= 21):
        season = "summer"
    elif (month == 9 and day >= 21):
        season = "fall"
    elif (month == 12 and day >= 21):
        season = "winter"
    else:
        if month in [1, 2, 3]:
            season = "winter"
        elif month in [4, 5, 6]:
            season = "spring"
        elif month in [7, 8, 9]:
            season = "summer"
        else:
            season = "fall"

    return season

try:
    month = int(input(""))
    day = int(input(""))
    print(get_season(month, day))
except ValueError:
    print("valueerror")