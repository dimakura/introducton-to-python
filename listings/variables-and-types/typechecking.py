# ANCHOR: type
x = 10
y = 20.0
z = 'hello'

print(type(x))
print(type(y))
print(type(z))
# ANCHOR_END: type

# ANCHOR: isinstance
print(isinstance(x, int))
print(isinstance(y, float))
print(isinstance(z, str))

print(isinstance(x, float))
print(isinstance(y, str))
print(isinstance(z, int))
# ANCHOR_END: isinstance
