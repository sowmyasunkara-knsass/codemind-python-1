T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    if Y > X:
        print("PROFIT")
    elif Y < X:
        print("LOSS")
    else:
        print("NEUTRAL")
