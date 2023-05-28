# Complex Conditions

Python allows you to combine multiple simple conditions into a single complex condition.

## `and` Operator

The `and` operator evaluates to `True` if both conditions are `True`, otherwise it evaluates to `False`.

```sh
>>> True and True
True

>>> True and False
False

>>> False and True
False

>>> False and False
False
```

Let's check when this might be useful:

File: `vote-by-country.py`:

```py
{{#include ../../listings/if-statement/vote-by-country.py:v1}}
```

which gives:

```txt
{{#include ../../listings/if-statement/vote-by-country.out:1}}
```

In this example, we specify the value of `age` to be `20`, which is enough to vote in almost any country. But in Cameroon, the voting age starts from `21`.

## `or` Operator

The `or` operator evaluates to `True` if either of the conditions is `True`, otherwise it evaluates to `False`.

```sh
>>> True or True
True

>>> True or False
True

>>> False or True
True

>>> False or False
False
```

Continuing with the previous example, Cameroon is not the only country with a voting age of `21`. For example, the same is true for Malaysia. Let's add this to our conditon:

```py
{{#include ../../listings/if-statement/vote-by-country.py:v2}}
```

which gives:

```txt
{{#include ../../listings/if-statement/vote-by-country.out:2}}
```

Note that we used parentheses to group the conditions. This ensures that the `or` operator is evaluated first (within parentheses), and then the `and` operator.
