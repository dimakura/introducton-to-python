languages = {'Python': 'Readable', 'C++': 'Fast', 'Java': 'Reliable', 'Rust': 'Safe'}

# ANCHOR: dict_loop
for language in languages:
    print(f"{language} is {languages[language].lower()}")
# ANCHOR_END: dict_loop

# ANCHOR: dict_items
for language, quality in languages.items():
    print(f"{language} is {quality.lower()}")
# ANCHOR_END: dict_items

# ANCHOR: dict_sorted_keys
for language in sorted(languages.keys()):
    print(f"{language} is {languages[language].lower()}")
# ANCHOR_END: dict_sorted_keys
