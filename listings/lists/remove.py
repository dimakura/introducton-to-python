from typing import List

# ANCHOR: start
list: List[int] = [1, 2, 3, 1, 5, 1]
print(list)
list.remove(1)
print(list)
# ANCHOR_END: start

# ANCHOR: remove-more
list.remove(3)
list.remove(1)
print(list)
# ANCHOR_END: remove-more
