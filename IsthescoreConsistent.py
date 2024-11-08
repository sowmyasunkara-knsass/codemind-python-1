x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    if (a<c and b<d) or (a<c and b<=d) or (a<=c and b<d) or (a==c and b==d):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
