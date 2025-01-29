T = int(input())
target = "ADVITIYA"

for _ in range(T):
    S = input()
    steps = sum(min(abs(ord(S[i]) - ord(target[i])), 26 - abs(ord(S[i]) - ord(target[i]))) for i in range(8))
    print(steps)
