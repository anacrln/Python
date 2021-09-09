"""Lambda anonymous,can take any number of arguments but it must take only a single expression or a single value.
"""

x = lambda i: i + 11
print(x(4))
print(x(8))


c = lambda i, y, z: i + y + z
print(c(5, 3, 2)) #10
print(c(6, 4, 1)) #11


def new(i):
  return lambda x: x * i

double = new(2)
triple = new(3)

print(double(5))#10
print(triple(5))#15
print(double(6), triple(6))#12 18


