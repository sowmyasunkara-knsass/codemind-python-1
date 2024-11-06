x = int(input()) 
lst = list(map(int,input().split()))
c=0
for i in range(x):
    if lst[i] % 2 == 0:    
        c += 1       
if c > (x - c):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
