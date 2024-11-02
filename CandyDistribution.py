x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if ((a//b)%2==0 and a%b==0):
        print("Yes")
    else:
        print("No")
