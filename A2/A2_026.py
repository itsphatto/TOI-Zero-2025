n = int(input())

fatahhrabitcount = 0
max_weight = -1
fattest_rabbit = ""

for j in range(n):
    name, weight = input().split()
    weight = int(weight)

    if weight > 15:
        fatahhrabitcount += 1

    if weight > max_weight:
        max_weight = weight
        fattest_rabbit = name

print(fatahhrabitcount)
print(fattest_rabbit, max_weight)