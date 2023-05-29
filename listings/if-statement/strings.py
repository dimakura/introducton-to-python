# ANCHOR: equality
car = 'Bmw'
print(car == 'Bmw')
# ANCHOR_END: equality

# ANCHOR: equality-2
print(car == 'Audi')
# ANCHOR_END: equality-2

# ANCHOR: equality-3
print(car == 'bmw')
# ANCHOR_END: equality-3

# ANCHOR: equality-4
print(car.lower() == 'bmw')
# ANCHOR_END: equality-4

# ANCHOR: inequality
print(car != 'Bmw')
print(car != 'Audi')
# ANCHOR_END: inequality
