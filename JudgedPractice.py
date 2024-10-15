T = int(input().strip())
for _ in range(T):
    responses = list(map(int, input().strip().split()))
    likes_count = sum(responses)
    if likes_count >= 4:
        print("YES")
    else:
        print("NO")
