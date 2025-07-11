def isCross(r1,r2,b1,b2):
    if r2 == b2: return True
    elif r1 == b1: return False
    elif r1[1] == b1[1]:
        if (b1[0] < r1[0] and b2[0] > r2[0]) or (b1[0] > r1[0] and b2[0] < r2[0]): ##############
            return True
        else: return False ###########
    else:
        if b1[0] < r2[0] and b2[0] > r1[0]: return True
    return False
inp = input().strip().split()
nRed = int(inp[0])
nBlue = int(inp[1])

inp = input().strip().split()
lRed = [(0,1)]
direction = 1

for i in inp:
    direction *= -1
    lRed.append((int(i),direction))

inp = input().strip().split()
lBlue = [(0, 1)]
direction = 1

for i in inp:
    direction *= -1
    lBlue.append((int(i), direction))

nCross = 1
for r in range(nRed):
    r1 = lRed[r]
    r2 = lRed[r+1]
    for b in range(nBlue):
        b1 = lBlue[b]
        b2 = lBlue[b+1]
        if isCross(r1,r2,b1,b2) : nCross += 1
        if b1[0] > r2[0]: break
print(nCross)


