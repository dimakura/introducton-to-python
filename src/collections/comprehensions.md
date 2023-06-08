# Comprensions

In previous chapter we have seen how to use [list comprehension](../loops/comprehensions.md) to create lists.
Comprehensions can also be used to create tuples, dictionaries, and sets.


## Dictionaries

```python
>>> {x: x*x for x in range(6)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Sets

```python
>>> {x*x for x in range(6)}
{0, 1, 4, 9, 16, 25}
```

## Tuples

In case of tuples, we need to use `tuple` function to convert the generator to tuple.

```python
>>> (x*x for x in range(6),)
<generator object <genexpr> at 0x7f8b1c0b3f10>

>>> tuple(x*x for x in range(6))
(1, 4, 9, 16, 25)
```
