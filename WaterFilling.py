x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    z = a+b+c
    if z<2:
        print("Water filling time")
    else:
        print("Not now")
