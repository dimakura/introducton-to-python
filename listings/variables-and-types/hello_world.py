# ANCHOR: start
# ANCHOR: var
message = "Hello, World!"
# ANCHOR_END: var
# ANCHOR: print
print(message)
# ANCHOR_END: print
# ANCHOR_END: start

# ANCHOR: print2
print(message.upper())
# ANCHOR_END: print2

# -- Using type hints --

# ANCHOR: typed
# ANCHOR: typed-var
message: str = "Hello, World!"
# ANCHOR_END: typed-var
print(message)
# ANCHOR_END: typed
