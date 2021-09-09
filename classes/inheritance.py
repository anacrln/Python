#Inheritance: create a class(Child) based on anoter class(Parent)

class Player:

  def __init__(self, fname, lname):#self=allow us to access variables from inside the class
    self.fname = fname
    self.lname = lname
class NewPlayer(Player):

  def __init__(self,fname,lname,total):
    Player.__init__(self,fname,lname)
    self.total = total

  def getDetails(self):
     return "%s %s has spent %s in total" % (self.fname, self.lname, self.total)

newP = NewPlayer("Dony", "Beckar", 1000)
print(newP.getDetails())