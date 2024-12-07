x = int(input())
for i in range(1,x+1):
    a,b,c,d = map(int,input().split())
    if a==(b+c+d):
        print("YES")
    elif a==b or a==c or a==d:
        print("YES")
    elif a==(b+c) or a==(b+d) or a==(c+d):
        print("YES")
    else:
        print("NO")
