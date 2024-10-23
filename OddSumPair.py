x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    if (a+b)%2!=0 or (b+c)%2!=0 or (a+c)%2!=0:
        print("YES")
    else:
        print("NO")
