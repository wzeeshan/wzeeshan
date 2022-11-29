splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
#or
print ("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")
#or
anotherString = """This string has been \
split over \
several \
lines"""

print(anotherString)

print("C:\\Apollo\\CDW250 CABOODLE DEVELOPMENT\\")
print(r"C:\Apollo\CDW250 CABOODLE DEVELOPMENT\notes.txt")

# Printing tabs
print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")
# or
number1 = "The Larch"
number2 = "The Horse Chestnut"

tbs = tabbedString = "Number 1\t" + number1
tbs2 = tabbedString = "Number 2\t" + number2
splt = splitString = tbs + "\n" + tbs2   

print(splt)
