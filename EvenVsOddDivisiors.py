x = int(input())
for i in range(1,x+1):
    a = int(input())
    c = 0
    res = 0
    for i in range(1,a+1):
        if a%i==0:
            if i%2==0:
                c = c+1
            else:
                res = res+1
    if c==res:
        print("0")
    elif c>res:
        print("1")
    else:
        print("-1")
