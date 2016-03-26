a = [2, 3, 4, 5, 6, 3, 4, 5,6]
b = []
[b.append(i) for i in a if not i in b]
print(b)
