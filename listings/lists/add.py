from typing import List

# ANCHOR: start
languages: List[str] = ['Python', 'C++']
print(languages)
# ANCHOR_END: start

# ANCHOR: append
languages.append('Java')
print(languages)
# ANCHOR_END: append

# ANCHOR: insert
languages.insert(0, 'C')
print(languages)
# ANCHOR_END: insert

# ANCHOR: insert-middle
languages.insert(2, 'Rust')
print(languages)
# ANCHOR_END: insert-middle