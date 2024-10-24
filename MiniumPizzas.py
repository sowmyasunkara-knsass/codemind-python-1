x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    z = a*b
    if z%4==0:
        print(z//4)
    else:
        if z%4<=4:
            print((z//4)+1)
        else:
            print((z//4)+(z%4))
