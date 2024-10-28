x = int(input())
for i in range(1,x+1):
    a,b,c,d = map(int,input().split())
    if (a-c)>(b-d):
        print("Second")
    elif (a-c)<(b-d):
        print("First")
    else:
        print("Any")
