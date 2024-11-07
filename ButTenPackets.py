x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if a>b:
        print((a*2)+(b*1))
    else:
        print((b*2)+(a*1))
