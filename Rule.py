x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if a<50:
        print("Z")
    elif a>=50 and b<50:
        print("F")
    else:
        print("A")
