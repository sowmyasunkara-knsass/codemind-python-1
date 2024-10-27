x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if a<=b:
        print("0")
    elif (a-b)<=4:
        print("1")
    elif (a-b)%4==0:
        print((a-b)//4)
    else:
        if a%4<=4:
            print(((a-b)//4)+1)
        else:
            print(((a-b)//4)+(a%4)//4)
