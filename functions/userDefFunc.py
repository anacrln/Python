#User defined functions
def multiplyFunc(x):
  result = x * x
  return result
print(multiplyFunc(6))
print(multiplyFunc(4))

#We can add multiple parameters(x, y, z)(3,6,9)

def multiplyFunc(x, y):
  multiply = x * y
  sum = x + y
  divide = x / y
  return multiply, sum, divide
print(multiplyFunc(10, 5))
print(multiplyFunc(9, 3))
