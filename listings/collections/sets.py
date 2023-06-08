# ANCHOR: set
fruits = {"apple", "banana", "cherry"}
# ANCHOR_END: set

# ANCHOR: set_function
fruits_from_list = set(["apple", "banana", "cherry"])
# ANCHOR_END: set_function

# ANCHOR: set_compare
print(fruits == fruits_from_list)
# ANCHOR_END: set_compare

# ANCHOR: set_empty
empty_set = set()
print(len(empty_set))
# => 0
# ANCHOR_END: set_empty

## ----

# We cheating a bit here, because the order of the elements
# in a set is not guaranteed.
fruits = sorted(list(fruits))

# ANCHOR: set_loop
for fruit in fruits:
    print(fruit)
# ANCHOR_END: set_loop

# back to set
fruits = set(fruits)

# ANCHOR: set_inclusion
print("banana" in fruits)
# => True

print("pineapple" in fruits)
# => False
# ANCHOR_END: set_inclusion

# ANCHOR: set_add
fruits.add("pineapple")
# => {"apple", "banana", "cherry", "pineapple"}

print("pineapple" in fruits)
# => True
# ANCHOR_END: set_add

# ANCHOR: set_update
fruits.update(["orange", "mango", "grapes"])
# => {"apple", "banana", "cherry", "pineapple", "orange", "mango", "grapes"}
# ANCHOR_END: set_update

# ANCHOR: set_remove
fruits.remove("banana")
# => {"apple", "cherry", "pineapple", "orange", "mango", "grapes"}
# ANCHOR_END: set_remove

fruits = sorted(list(fruits))
# ANCHOR: set_pop
fruit = fruits.pop()
print(fruit)
# => "pineapple" or any other element
# ANCHOR_END: set_pop
fruits = set(fruits)
