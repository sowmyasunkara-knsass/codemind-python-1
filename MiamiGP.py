for _ in range(T):
    X, Y = map(int, input().strip().split())
    max_allowed_time = 1.07 * X
    if Y <= max_allowed_time:
        print("YES")
    else:
        print("NO")
