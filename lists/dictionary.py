#don´t allow duplicates
person = {
  "name": "Fred",
  "age": 1,
  "country": "Brazil"
}
print(person)
print(len(person))#3
print(type(person))

x = person["name"] #or we can use x= person.get("name"), or x = person.keys()
print(x)
#x = person.values() will return (['Fred','1','Brazil'])
y = person.items() 
print(y)

if "name" in person:
  print("Yes, It's completed!")
  
person["age"] = 3 #to change a value.We can also use person.update({"age":3})
print(person)

#add a new item
person.update({"id": 21})
print(person)
#or person["id"] = 21
#or person.update({"id": 21, "number": 50})

#remove item
person.pop("age")
print(person)
#or person.popitem() remove the last item 
# del person will delete dictionary completely
#del person["age"]

#clear the dictionary
person.clear()
print(person)