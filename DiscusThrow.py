x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    if a>=b and a>c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    else:
        print(c)
