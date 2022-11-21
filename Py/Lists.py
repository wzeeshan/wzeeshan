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

#CODE1: Create an empty LIST
list1 = []
print("CODE1:")
print(f"list1 = {list1}")
print(f"data type = {type(list1)}")
print(f"length = {len(list1)}")
print()

#CODE2: Create LIST with 1 item
list2 = ["cloudacademy"]
print("CODE2:")
print(f"list2 = {list2}")
print(f"data type = {type(list2)}")
print(f"length = {len(list2)}")
print()

#CODE3: Create LIST with multiple items of the same type
list3 = [1, 2, 3, 4, 5]
print("CODE3:")
print(f"list3 = {list3}")
print(f"data type = {type(list3)}")
print(f"length = {len(list3)}")
print()

#CODE4: Create LIST with multiple items of different types
list4 = ["cloud", "academy", 1, True, False]
print("CODE4:")
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")
print(list4)
print()

#CODE5: Iterate over LIST with multiple items
print("CODE5:")
for item in list4:
  print(item)
print()
#CODE6: Search in LIST
print("CODE6:")
print ("cloud" in list4)
print ("blah" in list4)
print()

print("CODE7:")
item0 = list4[0]
item1 = list4[1]
print(f"item0 = {item0}")
print(f"item1 = {item1}")
print()

print("CODE8:")
list4[0] = "possible!!"
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")
print()

#CODE9: Append to LIST
print("CODE9:")
list4.append("new item")
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")
print()