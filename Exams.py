x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    z = a*b
    if (c/z)*100>50:
        print("YES")
    else:
        print("NO")
