k = input('')

amoutofcarrot, amountofcab, amountoftomato =  map(int, k.split())

carrot = 10
cabbish = 25
tomato = 3

finalcarrot = carrot * amoutofcarrot
finalcabbish = cabbish * amountofcab
finaltomato = tomato * amountoftomato

finalprice = finalcarrot + finalcabbish + finaltomato
print(finalprice)