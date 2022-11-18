from typing import List

a = []
b = [1, "string", True, 2.3]
var: list[int | str | bool | float] = b
print(var)

print("# append into list")
print("# value before append")
print(b[-4])
b.append("test")

print(var)
print("# value after append")
print(b[-4])

print("# insert into list")
b.insert(2, "newinsert")
print(var)

print(len(a))
print(len(b))

print('# starting and replacing value at index')
b[1:2] = ["replacedstring", 2]
print(var)
print(b[-6])

print("# delete value in list")
b[1:2] = []
print(var)
print(b[-6])

del (b[1])
print(var)
print(b[-2])

print("# list inside list")
c = [a, b]
print(a)
print(b)
print(c)
print("# index starts from left 0 or right -1")
print(c[1])
print(c[1][1])

print("# append list inside list")
c.append(c)
print(c[0])
print(c[1])
print(c[2])
print(c[2][1])
print(c[2][1][1])

print("# print(c[3]) this generates error")

print("# list can a duplicate values")
