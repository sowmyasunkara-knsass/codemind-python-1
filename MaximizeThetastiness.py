x = int(input())
for i in range(x):
    a, b, c, d = map(int, input().split())
    z = max(a, b) + max(c, d) 
    print(z)
