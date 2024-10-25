# Better Deal
x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if (100-a)<(200-(b*2)):
        print("FIRST")
    elif (100-a)>(200-(b*2)):
        print("SECOND")
    else:
        print("BOTH")
