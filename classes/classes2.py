#Class Methods and Constructors
#Methods= functions inside the class,functions that belongs to the object

class Person:
  """Create a new Person"""
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
  def new(self):
    print("Hi, my name is " + self.firstName)
    print("Hi, my name is " + self.lastName)

newPerson = Person("Ana", "Carolina")
anotherOne = Person("first", "last")

newPerson.new()