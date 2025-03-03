x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    area = 2*(a*b+b*c+c*a)
    print(1000//area)
