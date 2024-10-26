x = int(input())
for i in range(1,x+1):
    a,b,c,d = map(int,input().split())
    if a==0 and b==0 and c==0 and d==0:
        print("IN")
    else:
        print("OUT")
