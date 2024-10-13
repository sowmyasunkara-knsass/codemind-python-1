x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    if ((1*b)+(2*c))>=a:
        print("Qualify")
    else:
        print("NotQualify")
