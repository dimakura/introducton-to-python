# Sorting

In this section we will use the following list or unordered numbers:

```py
{{#include ../../listings/lists/sorting.py:list}}
```

What if we want to sort the list in ascending order? There are two ways to sort a list: temporarily and permanently.

During temporary sorting, the original list is not modified and a sorted copy is returned. Temporary sorting is done using the `sorted()` function.

```py
{{#include ../../listings/lists/sorting.py:temp}}
```

which gives us:

```txt
{{#include ../../listings/lists/sorting.out:1:2}}
```

Note, that the originl list, `numbers`, is not modified.

When sorting permanently, the original list is modified. Permanent sorting is done using the `sort()` method:

```py
{{#include ../../listings/lists/sorting.py:perm}}
```

with the original list changed:

```txt
{{#include ../../listings/lists/sorting.out:3}}
```

Note, that the in-place, permanent, sorting is more efficient than temporary sorting. On the other hand, temporary sorting is safer because it does not modify the original list.
