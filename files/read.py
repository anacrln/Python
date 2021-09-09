"""open(filname, mode)
r:read
a:append
w:write
x:create"""

#read
file = open("main.txt", "r")
print(file.read())
file.close#good practice

#we can put numbers inside the ()
print(file.read(9))
print(file.readable())
print(file.readline())

for x in file:
  print(x)
  file.close()

