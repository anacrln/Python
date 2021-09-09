#Items are unindexed an unordered

colors = {"orange", "yellow", "white"}
print(colors)
print(len(colors))#find out how many items it has

#if we repeat a value,it will not show up at the terminal
#Only change the whole set just like in te tuple
#Another way to write set function 
names = set(("Ana","Sophia","Cleoci", "Verci"))
newNames = set(("Romana","Apollo"))#if we had a list here,it would also bee concatenated
print(names)

#add items
names.add("Frederico")#only one argument per time
names.add("Pitoco")
print(names)

#we can add items by concatenating
names.update(newNames)
print(names)

#remove items
names.remove("Romana")#if we try to remove some item that doesn't exist,will return an error(keyError)
print(names)
#names.discard works too, but will not return an error if the item doesn't exist
#names.pop remove the last item,but in sets or tuples we don't know what is the last item,so we don't use here
#names.clear()
#del names=if we try print names before call the del function,the terminal will return an error


#Create a empty set:
names2 = set(())#we need use (()) if we want fill with items
print(type(names2))

#wrong way to create a empty set:
namesWrong = {}
print(type(namesWrong)) #it's class 'dict'

#you can't access items in sets
fruits = {"banana", "cherry", "pineapple"}

#print all items
for item in fruits:#could be any name: item,x,i...
  print(item)

#check if an item it is present in a set or not
print("banana" in fruits) #true
