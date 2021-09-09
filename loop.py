"""While is used to repeat a block of code based on a test expression"""
x = 1

while x < 7:
  print(x)
  x += 1 #or  x = x + 1

while x < 8:
  print(x)
  if x == 3:
   break
  x = x + 1

while x < 7:
    x = x + 1
    if x == 3:#will skip the 3
      continue
    print(x)
else:#if we use "break" we will not see the else part
  print("x is no longer less than 7!")

"""For is used to iterate over a sequence """

fruits = ["banana", "apple", "fig"]
for item in fruits:
  print(item)


fruit2 = "Banana"
for x in fruit2:
    print(x)
    if x == "n":
      break#or continue,then will print B a a a

#Range with for 
for x in range(7):#7 it's not included
#for x in range(3, 7)
# for x in range(3, 15, 2),here will start in 3,increasing 2 every time, run until 15
  print(x)
else:
  print("Completed")



