import math
def find_gcd(N, M):
    return math.gcd(N, M)
N, M = map(int, input().strip().split())
print(find_gcd(N, M))
