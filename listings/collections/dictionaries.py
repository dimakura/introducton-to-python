# ANCHOR: dict
languages = {'Python': 'Readable', 'C++': 'Fast', 'Java': 'Reliable', 'Rust': 'Safe'}
print(languages)
# ANCHOR_END: dict

# ANCHOR: dict_access
print(languages['Python'])
print(languages['C++'])
print(languages['Java'])
print(languages['Rust'])
# ANCHOR_END: dict_access

# ANCHOR: dict_get
print(languages.get('Python'))     # same as languages['Python']
print(languages.get('C') is None)  # key "C" does not exist
print(languages.get('C', 'Fun'))   # returns "Fun"
# ANCHOR_END: dict_get

# ANCHOR: dict_in
print('Python' in languages) # True
print('C' in languages)      # False
# ANCHOR_END: dict_in

# ANCHOR: dict_error
print(languages['C'])
# ANCHOR_END: dict_error
