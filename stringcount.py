def string_count(s):
    c = 0
    for char in s:
        c+=1
    return c
in_str = "Hello, world!"
length = string_count(in_str)
print(length)
