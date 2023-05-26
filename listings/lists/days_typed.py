# ANCHOR: list-type
# ANCHOR: import
from typing import List
# ANCHOR_END: import

# ANCHOR: var-declaration
days: List[str] = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# ANCHOR_END: var-declaration
print(type(days))
# ANCHOR_END: list-type

# ANCHOR: slice1
print(days[0:3])
# ANCHOR_END: slice1

# ANCHOR: slice2
print(days[:3])
# ANCHOR_END: slice2

# ANCHOR: slice3
print(days[3:7])
# ANCHOR_END: slice3

# ANCHOR: slice4
print(days[:])
# ANCHOR_END: slice4

# ANCHOR: out-of-range
days[7] # the last index is 6
# ANCHOR_END: out-of-range