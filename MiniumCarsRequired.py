x = int(input())
for i in range(1,x+1):
    a = int(input())
    if a<=4:
        print("1")
    elif a%4==0:
        print(a//4)
    else:
        if a%4<=4:
            print((a//4)+1)
        else:
            print((a//4)+(a%4)//4)
            
