# Comprehensions

List comprehensions are a way to create lists in a more concise way. They are a bit more advanced, so don't worry if you don't understand them right away.

In [previous section](./range.md) we wrote a loop to create a list of squares. Here's how we can do the same thing with a list comprehension:

```python
squares = [x ** 2 for x in range(1, 11)]
print(squares)
```

which outputs, as expected:

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

If you look carefully, list comprehensions are a bit like a reversed `for` loop.
