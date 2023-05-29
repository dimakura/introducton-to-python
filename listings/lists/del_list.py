# ANCHOR: start
names = ['Guido', 'Jukka', 'Ivan', 'Tim', 'Raymond']
del names[1]  # remove 'Jukka'
print(names)
# ANCHOR_END: start

# ANCHOR: del-slice
del names[1:3]  # remove 'Ivan' and 'Tim'
print(names)
# ANCHOR_END: del-slice
