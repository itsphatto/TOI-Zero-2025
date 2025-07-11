Pole = int(input())
Table = []

AL = 0
L = 0

for i in range(Pole):
    MyInp = int(input())
    Table.append(MyInp)

Sorted = sorted(Table)

for i in range(Pole):
    L += Sorted[i]
    AL += L * 2

print(AL)


