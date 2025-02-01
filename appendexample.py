s = "abaabcdcaba"
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(i)
    else:
        d[s[i]] = [i]
print(d)
