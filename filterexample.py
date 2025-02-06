str=input()
vow="aeiouAEIOU"
def is_vow(char):
    return char in vow
c=len(list(filter(is_vow,str)))
print(c)
