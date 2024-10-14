x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    if c%b == 0 and (c//b)<=a:
        print("YES")
    else:
        print("NO")
