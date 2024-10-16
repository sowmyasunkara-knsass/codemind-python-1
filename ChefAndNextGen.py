T = int(input())
results = []
for _ in range(T):
    A, B, X, Y = map(int, input().split())
    total_power_required = A * B
    total_power_available = X * Y
    
    if total_power_available >= total_power_required:
        results.append("Yes")
    else:
        results.append("No")
for result in results:
    print(result)
