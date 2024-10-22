x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    z = (a*1.1)-(a-b)
    print("%d"%(z))
