import math
def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n
n = int(input().strip())
if is_perfect_square(n):
    print("True")
else:
    print("False")
