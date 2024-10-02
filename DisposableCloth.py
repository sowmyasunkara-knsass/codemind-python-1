x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if a*100<b*10:
        print("Disposable")
    else:
        print("Cloth")
