x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    y = b//a
    z = max(0,c-y)
    print(z)
