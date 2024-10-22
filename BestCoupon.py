x = int(input())
for i in range(1,x+1):
    a = int(input())
    if a*0.1>=100:
        b = a*0.1
        print("%d"%b)
    else:
        print(100)
