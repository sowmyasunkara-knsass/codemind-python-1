t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    chairs = list(map(int, input().split()))
    chairs.sort()
    ved_chair = chairs[-1]
    varun_chairs = sum(chairs[:-1])
    
    ved_height = k + ved_chair
    varun_height = p + varun_chairs
    
    if ved_height > varun_height:
        print("Ved")
    elif varun_height > ved_height:
        print("Varun")
    else:
        print("Equal")
