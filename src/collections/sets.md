# Sets

Sets are much like lists, but they can only contain unique values.
Also, sets are unordered, so you cannot access them by index.

## Creating a set

To create a set you can use the `{}` syntax.

```python
{{#include ../../listings/collections/sets.py:set}}
```

Another way would be to use the `set()` function. When using the `set()` function, you can pass in an iterable, like a list, as an argument.


```python
{{#include ../../listings/collections/sets.py:set_function}}
```

In both examples we will get the same result:

```python
{{#include ../../listings/collections/sets.py:set_compare}}
# => True
```

The `set` function can also be used to create an empty set:

```python
{{#include ../../listings/collections/sets.py:set_empty}}
```

We canno use the `{}` syntax to create an empty set, because it would create an empty dictionary instead.

## Accessing set items

We cannot access set items by index, because sets are unordered.

But we can loop over the set and print each item:

```python
{{#include ../../listings/collections/sets.py:set_loop}}
```

which produces (not necessarily in this order):

```text
{{#include ../../listings/collections/sets.out:2:4}}
```

We can also test if an item is in a set:

```python
{{#include ../../listings/collections/sets.py:set_inclusion}}
```

## Add items to a set

To add items to a set, we can use the `add()` method:

```python
{{#include ../../listings/collections/sets.py:set_add}}
```

Another way would be to use the `update()` method, which takes an iterable as an argument:

```python
{{#include ../../listings/collections/sets.py:set_update}}
```

## Remove items from a set

You can use the `remove()` method to remove an item from a set:

```python
{{#include ../../listings/collections/sets.py:set_remove}}
```

If you need to remove any item from a set, you can use the `pop()` method:

```python
{{#include ../../listings/collections/sets.py:set_pop}}
```

## Set operations

Sets have a lot of useful methods to perform set operations.

### Union

To get the union of two sets, you can use the `union()` method:

```python
{1, 2, 3}.union({3, 4, 5})
# => {1, 2, 3, 4, 5}
```

Or, alternatively, you can use the `|` operator:

```python
{1, 2, 3} | {3, 4, 5}
# => {1, 2, 3, 4, 5}
```

### Intersection

To get the intersection of two sets, you can use the `intersection()` method:

```python
{1, 2, 3}.intersection({3, 4, 5})
# => {3}
```

Or, alternatively, you can use the `&` operator:

```python
{1, 2, 3} & {3, 4, 5}
# => {3}
```

Related to intersection are the `isdisjoint()` and `issubset()` methods. For example,

```python
{1, 2, 3}.isdisjoint({10, 11, 12})
# => True (because there are no common elements)

{1, 2, 3}.isdisjoint({3, 4, 5})
# => False (because 3 is in both sets)
```

```python
{1, 2, 3}.issubset({3, 4, 5})
# => False (because not all elements of the first set are in the second set)

{1, 2, 3}.issubset({1, 2, 3, 4, 5})
# => True (because all elements of the first set are in the second set)
```

### Difference

You can get difference of two sets using the `difference()` method:

```python
{1, 2, 3}.difference({3, 4, 5})
# => {1, 2}
```

Note that the operation is not commutative:

```python
{3, 4, 5}.difference({1, 2, 3})
# => {4, 5}
```

Alternatively, you can use the `-` operator:

```python
{1, 2, 3} - {3, 4, 5}
# => {1, 2}
```
