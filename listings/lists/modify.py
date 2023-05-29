# ANCHOR: list
numbers = [1, 2, 3, 4, 5]
print(numbers)
# ANCHOR_END: list

# ANCHOR: assign
numbers[0] = 10
numbers[-1] = numbers[-1] * 10
print(numbers)
# ANCHOR_END: assign

# ANCHOR: slice
numbers[1:4] = [33]
print(numbers)
# ANCHOR_END: slice
