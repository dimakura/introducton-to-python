# Reverse Order

You can reverse the order of a list by calling the `reverse()` method on the list. This method changes the order of the list permanently, but you can revert to the original order anytime by applying `reverse()` to the same list a second time.

File: `reverse.py`:

```py
{{#include ../../listings/lists/reverse.py:reverse}}
```

The first `print` statement outputs the original `numbers` list.

```txt
{{#include ../../listings/lists/reverse.out:1}}
```

Note the way we created this list. `range(1, 6)` creates an _iterator_ that produces the numbers `1` through `5` (`6` is not included). Then the `list()` function converts the iterator to a list.

The first call to `reverse()` changes the order of the list permanently. This can be seen in the output:

```txt
{{#include ../../listings/lists/reverse.out:2}}
```

The second call to `reverse()` changes the order of the list back to the original order:

```txt
{{#include ../../listings/lists/reverse.out:3}}
```

As it was the case with sorting we can also reverse the order of a list temporarily by using the `reversed()` class.

```py
{{#include ../../listings/lists/reverse.py:temp}}
```

One important point here is that `reversed()` produces an iterator. We can convert it to a list by using the `list()` function.

If we now print it:

```py
{{#include ../../listings/lists/reverse.py:reversed}}
```

we get numbers in reverse order:

```txt
{{#include ../../listings/lists/reverse.out:4}}
```

Note, that the original list, `numbers`, is not modified.

In place reversal is usually more efficient than temporary reversal. On the other hand, temporary reversal is safer because it does not modify the original list. In addition, temporary reversal is _lazy_, meaning it does not perform any work until it is needed.
