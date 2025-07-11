N = int(input())
prices = list(map(int, input().split()))

sum_set = set()

for start in range(N):
    total = 0
    for end in range(start, N):
        total += prices[end]
        sum_set.add(total)

print(len(sum_set))
