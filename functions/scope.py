x = 10 #here "x" is global
def new():
  #global
  x = 20
  print(x)# it we print inside the function,will return the "new" scope
new()
print(x) #if we print outside the function,will return the global value for x

#if we put "global" inside the "new" function,that "x" value will become global.

 


