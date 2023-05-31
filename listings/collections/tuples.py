# ANCHOR: fruit_tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
# ANCHOR_END: fruit_tuple

# ANCHOR: tuple_index
print(fruits[0])
print(fruits[1])
print(fruits[2])
# ANCHOR_END: tuple_index

# ANCHOR: tuple_index_negative
print(fruits[-1])
# ANCHOR_END: tuple_index_negative

# ANCHOR: tuple_immutable
fruits[0] = "pear"
# ANCHOR_END: tuple_immutable
