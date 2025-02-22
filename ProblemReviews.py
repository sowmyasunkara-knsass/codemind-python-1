x = int(input())
for i in range(x):
    a = int(input())
    b = list(map(int,input().split()))
    if all(c>4 for c in b):
        print("YES")
    else:
        print("NO")
