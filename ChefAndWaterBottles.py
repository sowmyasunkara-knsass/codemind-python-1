T = int(input().strip())
for _ in range(T):
    N, X, K = map(int, input().strip().split())
    max_fillable_bottles = K // X
    result = min(N, max_fillable_bottles)
    print(result)
