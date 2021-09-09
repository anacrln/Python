"""
x = 2
y = 4

print(x < 3 and x < 5)
print(x < 1 and x < 5)
print(x < 1 or x < 5)
print(not True)
print(not False)
print(not( x < 3 and x < 9))
"""
#identity operators
list1 = ["fig", "apple"]
list2 = ["fig", "apple"]
list3 = list2
#the "is" operator will return true if the objects are the same
print(list1 is list2)#false,they are the same value but not the same object

print(list3 is list2)

print(list1 is not list2)

#membership operators
#check if an item is present in an object
print("fig" in list1)
print("banana" in list1)
print("banana" not in list1)


