# ANCHOR: dict
students = {}

students['Alice'] = 20 # {'Alice': 20}
students['Bob'] = 19   # {'Alice': 20, 'Bob': 19}
# ANCHOR_END: dict

# ANCHOR: dict_update
students.update({'Alice': 22, 'Charlie': 25, 'Daniel': 23})
# ANCHOR_END: dict_update
print(students)

# ANCHOR: dict_delete
del students['Alice']
# ANCHOR_END: dict_delete

# ANCHOR: dict_popitem
print(students.popitem())
# ANCHOR_END: dict_popitem

# ANCHOR: dict_pop
print(students.pop('Bob', 33)) # => 19 (Bob's points)
print(students.pop('Bob', 33)) # => 33 (default value)
# ANCHOR_END: dict_pop

# ANCHOR: dict_del
del students['Charlie']
# ANCHOR_END: dict_del