# Conditional Tests

Before dealing with `if` statements, we need to understand conditional tests.

Conditional tests are expressions that can be evaluated as `True` or `False`. Both `True` and `False` are special values that belong to the `bool` type.

## Comparing Strings

We can test whether two strings are equal by using the equality operator `==`. Note that the equality operator is different from the assignment operator `=`.

Let's start with a simple example:

File: `strings.py`:

```py
{{#include ../../listings/if-statement/strings.py:equality}}
```

which produces:

```txt
{{#include ../../listings/if-statement/strings.out:1}}
```

Here our conditional test evaluates to `True` because the two strings are equal. If we change the value on the right-side of the equality operator to something else, the test will evaluate to `False`:


```py
{{#include ../../listings/if-statement/strings.py:equality-2}}
# {{#include ../../listings/if-statement/strings.out:2}}
```

Equality operator is case-sensitive. For example, the following test also evaluates to `False`:

```py
{{#include ../../listings/if-statement/strings.py:equality-3}}
# {{#include ../../listings/if-statement/strings.out:3}}
```

This is because variable `car` contains the string `Bmw` with a capital `B`, while the string literal on the right-side of the equality operator contains the string `bmw` with a lowercase `b`.

If our intention was to compare the two strings without considering the case, we can use the `lower()` method to convert variable `car` to lowercase before comparison:

```py
{{#include ../../listings/if-statement/strings.py:equality-4}}
# {{#include ../../listings/if-statement/strings.out:4}}
```

### Checking for Inequality

We can check whether two strings are not equal by using the inequality operator `!=`:

```py
{{#include ../../listings/if-statement/strings.py:inequality}}
# {{#include ../../listings/if-statement/strings.out:5}}
# {{#include ../../listings/if-statement/strings.out:6}}
```

## Numerical Comparisons

As with strings, we can compare numbers using the equality and inequality operators:

```py
{{#include ../../listings/if-statement/numbers.py:numbers}}
```

which prints:

```txt
{{#include ../../listings/if-statement/numbers.out:1:2}}
```

Additionally, we can use less or greater than operators to check whether a number is less than or greater than another number:

```py
{{#include ../../listings/if-statement/numbers.py:less-than}}
# {{#include ../../listings/if-statement/numbers.out:3}}

{{#include ../../listings/if-statement/numbers.py:greater-than}}
# {{#include ../../listings/if-statement/numbers.out:4}}
```

Two more operators to compare numbers are `<=` and `>=` which check whether a number is less than or equal to, or greater than or equal to another number:

```py
{{#include ../../listings/if-statement/numbers.py:less-than-equal}}
# {{#include ../../listings/if-statement/numbers.out:5}}

{{#include ../../listings/if-statement/numbers.py:greater-than-equal}}
# {{#include ../../listings/if-statement/numbers.out:6}}
```

## Boolean Variable

One special case of conditional tests is a boolean variable. A boolean variable has type `bool` and can be either `True` or `False`. For example:

```py
breakfast_ready: bool = True
game_over: bool = False
```
