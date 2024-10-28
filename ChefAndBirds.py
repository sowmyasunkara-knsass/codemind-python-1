x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    if c%a==0 and c%b!=0:
        print("CHICKEN")
    elif c%a!=0 and c%b==0:
        print("DUCK")
    elif c%a==0 and c%b==0:
        print("ANY")
    else:
        print("NONE")
