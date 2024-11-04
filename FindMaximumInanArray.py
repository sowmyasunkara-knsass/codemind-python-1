x = int(input())
for i in range(1,x+1):
    a = int(input())
    lst = list(map(int,input().split()))
    print(max(lst))
