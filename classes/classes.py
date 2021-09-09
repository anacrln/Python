"""A class is a prototype or a code template from wich objects are created
An object ia an instance of a class
We can define a class using the class keyword
class ClassName:
    statements"""

class Person:
  """Create a new Person"""
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
newPerson = Person("Ana", "Carolina")
anotherOne = Person("first", "last")

#Displayind the output
print(newPerson)
print(newPerson.firstName)
print(newPerson.lastName)
#The numbers that appear on the terminal are the memory location where that data is saved 

print(anotherOne.firstName)
print(anotherOne.lastName)

#Objects Modifications

newPerson.firstName = "Cris"
newPerson.lastName = "Ronaldo"

print(newPerson.firstName, newPerson.lastName)

#Delete: del newPerson.firstName
#del newPerson will delete all
