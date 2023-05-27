from typing import List

# ANCHOR: start
numbers: List[int] = [1, 2, 3, 4, 5]

print(numbers)         # original list
# ANCHOR: pop
print(numbers.pop())   # removing last element
# ANCHOR_END: pop
print(numbers)         # list after pop
# ANCHOR_END: start

# ANCHOR: pop-index
print(numbers.pop(0))  # removing first element
print(numbers)
# ANCHOR_END: pop-index
