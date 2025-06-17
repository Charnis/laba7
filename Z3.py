m = [-13, 12, 11, 15, -3, -2, 1, 2, 3, -14, 23]
m.sort()
result = []
for i in m:
    if 10 <= i <= 99 and i > 0:
        result.append(i)
result.sort()
print(result)