# ANCHOR: loop
animals = ['cat', 'dog', 'monkey']

for animal in animals: # assign next value to animal
    print(animal)      # print animal
# ANCHOR_END: loop


# ANCHOR: loop-2
for animal in animals:
    greeting = f"Hello, {animal.title()}!"
    print(greeting)
# ANCHOR_END: loop-2

# ANCHOR: loop-3
for animal in animals:
    greeting = f"Hello, {animal.title()}!"
print(greeting)
# ANCHOR_END: loop-3