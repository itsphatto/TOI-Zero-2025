matrices = []

for m in range(5):
    matrices.append(list(map(int, input().split())))

eRow = -1
eColumn = -1

for i in range(5):
    if sum(matrices[i]) % 2 != 0: # checking for even numbers
        eRow = i
        break

for j in range(5):
    Columnsum = 0
    for i in range(5):
        Columnsum += matrices[i][j]
    if Columnsum % 2 != 0:
        eColumn = j
        break

print(eRow, eColumn)