X = int(input())
max_sixes = min(X // 6, 100)
while max_sixes >= 0:
    remaining_runs = X - max_sixes * 6
    remaining_balls = 100 - max_sixes
    if 0 <= remaining_runs <= remaining_balls * 4:
        print(max_sixes)
        break
    max_sixes -= 1
