"""
fruits = ["banana","tomato","lemon"]
numbers = [2, 4, 6]

fruits[2] = "Cherry"
print(fruits[2])
print(fruits)

fruits[0:2] = ["orange","melon"]
print(fruits)#index 2 it's not included

fruits.insert(1,"watermelon")
print(fruits)

fruits.append("apple")#add something to the end of list
print(fruits)

newFruits = ["pineapple", "mango", "strawberry"]
fruits.extend(newFruits)
print(fruits)
"""

fruits = ["banana","tomato","lemon"]
fruits.remove("tomato")
print(fruits)
#we can use remove or pop(remove the last item) to remove items.
#del fruits[2] also delete
#fruits.clear() delete all items,if we print will show []
