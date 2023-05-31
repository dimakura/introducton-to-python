# Tuples

Tuple is a collection of items of any type. It is immutable, which means that once created, it cannot be modified. Otherwise, it is very similar to a list.

As usual, let's start with a simple example:

```python
{{#include ../../listings/collections/tuples.py:fruit_tuple}}
```

which produces the following output:

```txt
{{#include ../../listings/collections/tuples.out:1}}
```

You can access tuple items by index, just like with lists:

```python
{{#include ../../listings/collections/tuples.py:tuple_index}}
```

which gives:

```txt
{{#include ../../listings/collections/tuples.out:2:4}}
```

As with lists, you can use negative indices to access items from the end of the tuple:

```python
{{#include ../../listings/collections/tuples.py:tuple_index_negative}}
```

which prints:

```txt
{{#include ../../listings/collections/tuples.out:5}}
```

But unlike lists, tuples are immutable, which means that you cannot modify them. For instance, if you try to assign a new value to an item:

```python
{{#include ../../listings/collections/tuples.py:tuple_immutable}}
```

you will get an error:

```txt
{{#include ../../listings/collections/tuples.out:6:10}}
```

## Tuple methods

To check if an item is in a tuple, you can use the `in` operator:

```python
{{#include ../../listings/collections/tuples2.py:tuple_in}}
```

which produces:

```txt
{{#include ../../listings/collections/tuples2.out:1:2}}
```

Note also that in the example above, we have the value `1` twice in the tuple. Tuples, as lists, can contain duplicate items.

To obtain size of a tuple, you can use the `len()` function:

```python
{{#include ../../listings/collections/tuples2.py:tuple_len}}
# => {{#include ../../listings/collections/tuples2.out:3}}
```

## Tuple type

To see type of the tuple, you can use the `type()` function, as usual:

```python
{{#include ../../listings/collections/tuples2.py:tuple_type}}
# => {{#include ../../listings/collections/tuples2.out:4}}
```

One interesting case of a tuple is a tuple with a single item. In this case, you need to add a comma after the item, otherwise Python will treat it as a regular value in parentheses:

```python
{{#include ../../listings/collections/tuples2.py:tuple_single}}
```

which prints:

```txt
{{#include ../../listings/collections/tuples2.out:5:6}}
```

## When to use tuples over lists

Prefer tuples over lists when you want to make sure that the collection is not modified. Tuples are generally faster and more memory efficient than lists.
