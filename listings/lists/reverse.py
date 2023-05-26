from typing import List

# ANCHOR: reverse
numbers: List[int] = list(range(1, 6))
print(numbers)

numbers.reverse() # reverse the list
print(numbers)

numbers.reverse() # reverse the list again
print(numbers)
# ANCHOR_END: reverse

# ANCHOR: temp
reversed_numbers: reversed = reversed(numbers)
# ANCHOR_END: temp

# ANCHOR: reversed
print(list(reversed_numbers))
# ANCHOR_END: reversed