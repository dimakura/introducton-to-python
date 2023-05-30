# Stats

Loops can be used to calculate statistics of a list (or an iterator) of numbers. Let's see how we can calculate the sum, minimum, and maximum of a list of numbers.

## Sum

To calculate sum of a list of numbers, we can use a `for` loop to iterate over the list and add each number to a variable that keeps track of the sum. Here's an example:

```py
{{#include ../../listings/loops/sum.py}}
```

Not that at the last line we also calculate the average of the numbers by dividing the sum by the length of the list.

Output of the program:

```txt
{{#include ../../listings/loops/sum.out}}
```

## Minimum and Maximum

Here's how we can calculate the minimum and maximum of a list of numbers:

```py
{{#include ../../listings/loops/min-max.py}}
```

We first initialize the minimum and maximum to the first element of the list. Then we iterate over the list and update the minimum and maximum if we find a smaller or larger number. Finally, we print the minimum and maximum:

```txt
{{#include ../../listings/loops/min-max.out}}
```

Notice how we use the `if` statement inside the `for` loop.

## Built-in Functions

In practice, we don't need to write our own functions to calculate the sum, minimum, and maximum of a list of numbers. Python provides built-in functions for these purposes. Here's how we could use them:

```py
{{#include ../../listings/loops/built-in.py}}
```

and here's the output:

```txt
{{#include ../../listings/loops/built-in.out}}
```

In general, in programming it's a good idea to use built-in functions whenever possible. They are usually faster and more reliable than our own functions.
