def split(k):
    coins = [10, 5, 2, 1]
    for coin in coins:
        count = k // coin
        k %= coin
        print(f"{coin} = {count}")

try:
    amount = int(input(""))
    split(amount)
except ValueError:
    print("error")
