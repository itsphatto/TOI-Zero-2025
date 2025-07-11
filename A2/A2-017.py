j = input().split() #first input size of ramen type of ramen
k = input().split()#second input

sizeramen = j[0]
typeoframen = j[1]

topping = k[0]
amountoftopping = int(k[1])

constant = 0

if sizeramen == 'S' and typeoframen == 'R':
    constant += 60
elif sizeramen == 'S' and typeoframen == 'T':
    constant += 80

elif sizeramen == 'M' and typeoframen == 'R':
    constant += 80
elif sizeramen == 'M' and typeoframen == 'T':
    constant += 100

elif sizeramen == 'L' and typeoframen == 'R':
    constant += 100
elif sizeramen == 'L' and typeoframen == 'T':
    constant += 120


if topping == 'N':
    constant += 0

elif topping == 'P':
    constant += 15 * amountoftopping

elif topping == 'E':
    constant += 10 * amountoftopping

print(constant)

