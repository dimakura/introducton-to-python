# For Loop

Let's start with an example.

Suppose we have a list of animals and we want to great each one of them. To begin with, we'll simply print each animal:

```python
{{#include ../../listings/loops/animals.py:loop}}
```

The first line of this program should be familiar by now; it creates a list of three animals.

What happens next is the interesting part. We use a `for` loop to iterate over the list of animals. Each time the loop executes, the variable `animal` will be assigned the next value in the list. The first time through the loop, `animal` will be assigned the value `'cat'`, the second time through the loop, `animal` will be assigned the value `'dog'`, and the third time through the loop, `animal` will be assigned the value `'monkey'`. The loop will terminate when there are no more values in the list.

At every step the loop performs the same action: it prints the value of `animal`. That's easy to see from the output of the program:

```text
{{#include ../../listings/loops/animals.out}}
```

Note that the action performed by the loop is indented. This is a requirement in Python. The indentation tells Python which statements are part of the loop. In this case we have a single statement, the `print` statement, but we could have had several statements, all indented to the same level.

An example of a program with few statements is given below:

```python
{{#include ../../listings/loops/animals.py:loop-2}}
```

with the output:

```txt
{{#include ../../listings/loops/animals.out:4:6}}
```

If we don't indent the second statements in the loop, we won't get any error. This still will be a valid Python program, but it will do something different:

```python
{{#include ../../listings/loops/animals.py:loop-3}}
```

The result of executing this program will be a single line, with the last value of `greeting`:

```txt
{{#include ../../listings/loops/animals.out:7}}
```
