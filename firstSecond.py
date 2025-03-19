a,b,c,d = map(int,input().split())
if abs(a-b)<abs(c-d):
    print("First")
elif abs(a-b)>abs(c-d):
    print("Second")
else:
    print("Both")
