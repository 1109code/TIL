a = [1, 2, 3]
b = [[1, 2, 4]]
if a not in b:
    b.append(a)
print(b)