import sys

print(sys.version, sys.platform)

a = 5
b = 125.54
c = 'Hello World!'

print(id(a))
print(sys.getsizeof(a))

print(id(b))
print(sys.getsizeof(b))

print(id(c))
print(sys.getsizeof(c))