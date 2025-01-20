x = int(input())
for i in range(1, x + 1):
    a, b = map(int, input().split())
    c = a + b
    count = 0
    for j in range(1, int(c**0.5) + 1):
        if c % j == 0:
            count += 1
            if j != c // j:
                count += 1
    if count == 2:
        print("Alice")
    else:
        print("Bob")
