x = int(input())
for i in range(1,x+1):
    p,a,q,b = map(int,input().split())
    if max(p,a)<max(q,b):
        print("P")
    elif max(q,b)<max(p,a):
        print("Q")
    else:
        print("TIE")
