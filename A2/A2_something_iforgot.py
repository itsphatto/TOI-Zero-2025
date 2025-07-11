L, P = map(int, input().split())
rabbit_jump, monkey_jump, frog_jump = map(int, input().split())

points = {}
for _ in range(P):
    pos, score = map(int, input().split())
    points[pos] = score

def calculate_score(jump):
    pos = 0
    score = 0
    while pos <= L:
        if pos in points:
            score += points[pos]
        pos += jump
    return score

rabbit_score = calculate_score(rabbit_jump)
monkey_score = calculate_score(monkey_jump)
frog_score = calculate_score(frog_jump)

scores = {
    "Rabbit": rabbit_score,
    "Monkey": monkey_score,
    "Frog": frog_score
}

max_score = max(scores.values())

for name in ["Rabbit", "Monkey", "Frog"]:
    if scores[name] == max_score:
        print(name, max_score)
