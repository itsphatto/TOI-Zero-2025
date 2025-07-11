i, j = input().split()
j = int(j)

A = ['R', 'G', 'B']

color = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}

start_index = A.index(i)

result = []

for c in range(j):
    current_color = A[(start_index + c) % 3]
    result.append(color[current_color])

print(" ".join(result))
