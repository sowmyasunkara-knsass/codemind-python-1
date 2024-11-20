def is_ugly_number(num):
    if num <= 0:
        return False
    for factor in [2, 3, 5]:
        while num % factor == 0:
            num //= factor
    return num == 1
num = int(input().strip())
if is_ugly_number(num):
    print("Ugly Number")
else:
    print("Not Ugly Number")
