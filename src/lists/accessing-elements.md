# Accessing Elements

Individual items in our list are called list elements. We can access them by their index. The index of the first element is `0`, the index of the second element is `1`, and so on.

To continue with our example from the previous section, we add one more line to `days.py` program:

```py
{{#include ../../listings/lists/days.py:second}}
```

which prints the first element of the list:

```py
{{#include ../../listings/lists/days.out:2}}
```

It would be nice to capitalize the first letter of the day. We can do this by using the `title()` method:

```py
{{#include ../../listings/lists/days.py:third}}
```

which looks much better:

```py
{{#include ../../listings/lists/days.out:3}}
```

We can now try to print more elements:

```py
{{#include ../../listings/lists/days.py:fourth}}
```

which prints:

```py
{{#include ../../listings/lists/days.out:3:5}}
```

One neat trick is to use negative indices. The index `-1` refers to the last element, `-2` refers to the second last element, and so on. Try it youself, by adding few more lines to the `days.py` program:

```py
{{#include ../../listings/lists/days.py:fifth}}
```

and check the output:

```py
{{#include ../../listings/lists/days.out:6:7}}
```

## List Type

Remember that we can check the type of a variable by using the `type()` function. Let's check the type of our list:

```py
{{#include ../../listings/lists/days.py:sixth}}
```

which produces:

```py
{{#include ../../listings/lists/days.out:8}}
```

Python correctly identifies our variable as a list even though we didn't explicitly specify it.
We could have been more explicit and specify the type of the variable using type hint:

```py
{{#include ../../listings/lists/days_typed.py:list-type}}
```

which would again produce the same output as before:

```py
{{#include ../../listings/lists/days_typed.out:1}}
```

We will prefer using type hints in the rest of the book. But remember that they are ignored by Python interpreter, so you can also omit them if you want.

Let's more closely analyze the code fragment above.

On the first list, we _import_ `List` class from a module called `typing`.

```py
{{#include ../../listings/lists/days_typed.py:import}}
```

We'll discuss modules and imports in more details later in this book. For now just remember that modules provide additional functionality to Python programs. We'll be using other classes from `typing` module throughout the book.

On the next line,

```py
{{#include ../../listings/lists/days_typed.py:var-declaration}}
```

we declare variable `days` to be of type `List` and initialize it with a list of strings.
Note that `List` has additional parameter `[str]` which means that the list will contain strings.
If we wanted to create a list of integers, we would use `List[int]` instead.

## Slicing

We can access multiple elements of a list with _slicing_.

Here we print the first three elements of the list:

```py
{{#include ../../listings/lists/days_typed.py:slice1}}
```

Instead of a single index we now use two indices separated by a colon. This has an effect of producing a new list which contains elements from the first index up to (but not including) the second index. In our example, we get a list which contains elements from index `0` up to (but not including) index `3`. Let's check the output:

```py
{{#include ../../listings/lists/days_typed.out:2}}
```

In the example above we could have omitted the first index and just write `days[:3]`. This would produce the same result.

```py
{{#include ../../listings/lists/days_typed.py:slice2}}
```

If we wanted to get a list of remaining days, we could write:

```py
{{#include ../../listings/lists/days_typed.py:slice3}}
```

Note that we use `7` as the second index. This is because the second index is not included in the result, and the last index we want to select is `6`. The result is:

```py
{{#include ../../listings/lists/days_typed.out:4}}
```

You could also omit the second index and just write `days[3:]` if you want all remaining elements.

One more trick is to omit both indices. This will produce a copy of the original list:

```py
{{#include ../../listings/lists/days_typed.py:slice4}}
```

which outputs:

```txt
{{#include ../../listings/lists/days_typed.out:5}}
```

## Out of Range Error

If we try to access an element by index which is too large, we get an error:

For example:

```py
{{#include ../../listings/lists/days_typed.py:out-of-range}}
```

produces:

```txt
{{#include ../../listings/lists/days_typed.out:6:10}}
```

"Out of range" error is a common error in programming.
