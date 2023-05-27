from typing import List

# ANCHOR: list
numbers: List[int] = [7, 8, 1, 6, 5, 4, 3, 2, 10, 9]
# ANCHOR_END: list

# ANCHOR: temp
sorted_numbes: List[int] = sorted(numbers) # sorted copy
print(sorted_numbes) # print sorted numbers
print(numbers)       # print original list
# ANCHOR_END: temp

# ANCHOR: perm
numbers.sort() # sort in place
print(numbers)
# ANCHOR_END: perm
