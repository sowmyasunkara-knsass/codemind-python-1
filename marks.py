names = ["berlin", "rio", "tokyo", "palermo", "lison", "professor"]
marks = [[68, 49, 86, 39, 71],
         [58, 58, 33, 38, 90],
         [25, 77, 32, 96, 39],
         [42, 65, 30, 51, 92],
         [83, 31, 73, 25, 73],
         [74, 42, 72, 51, 29]]
base_d = dict(zip(names,marks))
d1 = {}
d2 = {}
d3 = {}
d4 = {}
for k,v in base_d.items():
    d1[k] = max(v)
    d2[k] = min(v)
    d3[k] = sum(v)
    d4[k] = [max(v),min(v),sum(v)]
print(d1,d2,d3,d4, sep = '\n')
