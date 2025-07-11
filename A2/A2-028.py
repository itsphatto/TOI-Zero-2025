n = int(input())

num1 = input()
num2 = input()

not_9_count = 0

for i in range(n):
    digit_sum = int(num1[i]) + int(num2[i])
    if digit_sum != 9:
        not_9_count += 1

if not_9_count == 0:
    print("YES")
else:
    print(f"NO {not_9_count}")

