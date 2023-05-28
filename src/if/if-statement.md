# If Statement

## Simple if Statement

In it's simplest form, an `if` statement looks like this:

```py
if conditional_test:
    # do something
```

if `conditional_test` evaluates to `True`, then the indented code block is executed. If it evaluates to `False`, then the indented code block is skipped.

Python uses indentation to determine which lines of code are associated with the `if` statement. All indented lines after the `if` statement are considered part of the code block. The code block ends when the indentation returns to the same level as the `if` statement.

```py
if conditional_test:
    # do something
    # do something else

# code block ends here
```

Let's see this in practice:

```py
{{#include ../../listings/if-statement/simple-if.py}}
```

with output:

```txt
{{#include ../../listings/if-statement/simple-if.out}}
```

Try to change the value of `car` to something else and see what happens.

## if-else Statement

A more elaborate form of the `if` statement is the `if-else` statement. It looks like this:

```py
if conditional_test:
    # do something
else:
    # do something different
```

It allows you to specify an alternative action if the `conditional_test` evaluates to `False`.

For example,

```py
{{#include ../../listings/if-statement/if-else.py}}
```

produces output:

```txt
{{#include ../../listings/if-statement/if-else.out}}
```

## if-elif-else Statement

The `if-elif-else` statement allows you to specify multiple alternative actions.
It's allowed to have multiple `elif` statements, but only one `else` statement.

```py
if conditional_test_1:
    # do something
elif conditional_test_2:
    # do something different
elif conditional_test_3:
    # do something event more different
else:
    # do something else
```

We can now write more ellaborate classification of cars:

```py
{{#include ../../listings/if-statement/if-elif-else.py}}
```

```txt
{{#include ../../listings/if-statement/if-elif-else.out}}
```

In this example, once `car.lower() == "mercedes"` evaluates to `True`, the rest of the `elif` statements, and the `else` statement, are skipped.

The `else` statement is optional. It is used to specify an action if none of the `if` or `elif` statements evaluate to `True`. And it must be the last statement in the `if` statement.
