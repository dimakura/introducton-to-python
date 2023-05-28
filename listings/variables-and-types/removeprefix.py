# ANCHOR: prefix
url = 'https://dimakura.github.io'
print(url.removeprefix('https://'))
# ANCHOR_END: prefix

# ANCHOR: suffix
print(url.removesuffix('.github.io'))
# ANCHOR_END: suffix

# ANCHOR: prefix-suffix
print(url.removeprefix('https://').removesuffix('.github.io'))
# ANCHOR_END: prefix-suffix
