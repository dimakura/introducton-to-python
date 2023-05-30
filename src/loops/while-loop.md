# While Loop

For-loops are great for iterating over a fixed number of elements. But what if you don't know how many elements you need to iterate over? In this case, you can use a while-loop.

Syntax of a while loop:

```python
while condition:
    # do something
```

The _body_ of the while loop will be performed until `condition` is satisfied.

Let's see an example:

```py
{{#include ../../listings/loops/while-loop.py}}
```

Here, we start with the value of `num` be equal to `1`. We first check that the value of `num` is less than or equal to `10`. If this is true, we print the value of `num` and then increment it by `1` (notice `+=`). Thus, on the second iteration, the value of `num` will be `2`. This process will continue until the value of `num` is `10`. At this point, the condition `num < 10` will be false and the while loop will terminate.

Therefore, the output should be the numbers from `1` to `9` (but not `10`):


```txt
{{#include ../../listings/loops/while-loop.out}}
```
