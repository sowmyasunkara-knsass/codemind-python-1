x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    z = b/a
    if z>=0.75:
        print("YES")
    else:
        print("NO")
