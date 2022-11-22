def add(a, b):
    result = a + b
    return result

print(add(6, 2))

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("Pakistan")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)