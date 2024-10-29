x = int(input())
for i in range(1,x+1):
    a,b,c,d = map(int,input().split())
    print(a+(b-c)*d)
