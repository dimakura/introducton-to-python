# ANCHOR: tuple_in
numbers = (1, 2, 3, 1)

print(1 in numbers)
print(4 not in numbers)
# ANCHOR_END: tuple_in

# ANCHOR: tuple_len
print(len(numbers))
# ANCHOR_END: tuple_len

# ANCHOR: tuple_type
print(type(numbers))
# ANCHOR_END: tuple_type

# ANCHOR: tuple_single
single_value = (1)
print(type(single_value))

a_tuple = (1,)
print(type(a_tuple))
# ANCHOR_END: tuple_single
