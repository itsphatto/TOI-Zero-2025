j = input().split() #first input
k = input().split()#second input
Bobatype = j[0]
AmountofBoba = int(j[1])
TeaType = k[0]
Sweetnesslevel = k[1]
AmoutofTea = int(k[2])

constant = 0

if Bobatype == 'H':
    constant += 5 * AmountofBoba
elif Bobatype == 'O':
    constant += 3 * AmountofBoba
elif Bobatype == 'J':
    constant += 2 * AmountofBoba
# end of bobatype calculation

if TeaType == 'R':
    if Sweetnesslevel == '1':
        constant += 12 * AmoutofTea
    if Sweetnesslevel == '2':
        constant += 18 * AmoutofTea
    if Sweetnesslevel == '3':
        constant += 25 * AmoutofTea
elif TeaType  == 'T':
    if Sweetnesslevel == '1':
        constant += 15 * AmoutofTea
    if Sweetnesslevel == '2':
        constant += 20 * AmoutofTea
    if Sweetnesslevel == '3':
        constant += 30 * AmoutofTea
elif TeaType == 'M':
    if Sweetnesslevel == '1':
        constant += 10 * AmoutofTea
    if Sweetnesslevel == '2':
        constant += 15 * AmoutofTea
    if Sweetnesslevel == '3':
        constant += 20 * AmoutofTea

print(constant)

