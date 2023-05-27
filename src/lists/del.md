# `del` Operator

Python's `del` operator is used to delete an object. It can be used to delete a variable, a list, or a part of a list (slice).

## Deleting a Variable

We've already seen how to declare a variable.

Filename: `del.py`

```py
{{#include ../../listings/lists/del.py:var}}
```

This outputs a number:

```py
{{#include ../../listings/lists/del.out:1}}
```

Actually, we can delete the variable `a` using the `del` operator.

```py
{{#include ../../listings/lists/del.py:del}}
```

Deletion is the opossite of declaration. The variable `a` does not exist anymore! So, if we try to print it:

```py
{{#include ../../listings/lists/del.py:del-error}}
```

System will throw an error:

```txt
{{#include ../../listings/lists/del.out:2:}}
```

## Delete an Item from a List

You can use `del` to delete an item from a list. This looks pretty much like `pop()` method which we discussed in the [previous section](./modifying-lists.md#removing-elements-from-a-list), but `del` does not return the deleted item.

Filename: `del_list.py`

```py
{{#include ../../listings/lists/del_list.py:start}}
```

This outputs:

```py
{{#include ../../listings/lists/del_list.out:1}}
```

## Delete a Slice from a List

`del` can also be used to delete a slice from a list. This makes `del` more powerful than `pop()` method.

Here's an example:

```py
{{#include ../../listings/lists/del_list.py:del-slice}}
```

which gives:

```py
{{#include ../../listings/lists/del_list.out:2}}
```
