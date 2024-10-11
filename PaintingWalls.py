x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    m = a*b
    n = c//2
    z = n//m
    print(z)
