x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if 2*b>a:
        print("0")
    else:
        print(a//(2*b))
