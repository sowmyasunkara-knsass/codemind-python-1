T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    total_water = sum(A)
    min_bottles = (total_water + X - 1) // X
    print(min_bottles)
