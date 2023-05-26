# Modifying Lists

It's often necessary to modify lists after they've been created. You can easily add to or remove items from a list, and you can modify individual items in a list as well.

## Adding Elements to a List

We begin with a list of favorite programming languages,

```py
{{#include ../../listings/lists/add.py:start}}
```

which produces the following output:

```txt
{{#include ../../listings/lists/add.out:1}}
```

There are two ways to add a new element into this list. The first is to use the `append()` method, which adds the new element to the end of the list:

```py
{{#include ../../listings/lists/add.py:append}}
```

The output is:

```txt
{{#include ../../listings/lists/add.out:2}}
```

You should usually prefer `append()` to add elements to a list, because it's very efficient.

In comparison, the `insert()` method is less efficient, but it gives you more flexibiliy. Using `insert()`, you can add a new element at any position in your list by specifying the index of the new item. For example, to add the new language `'C'` at the beginning of the list, you would use the following code:

```py
{{#include ../../listings/lists/add.py:insert}}
```

which produces the following output:

```txt
{{#include ../../listings/lists/add.out:3}}
```

If you need to add a new programming language exactly in the middle of the list, you can use the `insert()` again:

```py
{{#include ../../listings/lists/add.py:insert-middle}}
```

with the result:

```txt
{{#include ../../listings/lists/add.out:4}}
```

## Removing Elements from a List

Now consider a problem when you want to remove an item from a list.

There are two main ways to go about this task, depending on whether you know the position of the item you want to remove or you know its value.

Let's begin with the case where you know the position of the item you want to remove. You can use `pop()` method for this.

Let's see an example:

```py
{{#include ../../listings/lists/pop.py:start}}
```

which produces the following output:

```txt
{{#include ../../listings/lists/pop.out:1:3}}
```

Notice the line where we `pop()`ed the element:

```py
{{#include ../../listings/lists/pop.py:pop}}
```

In this case the last element is removed. And usually, you should prefer to use `pop()` in this way, because it's very efficient.

There's another way to use `pop()`. If you want to remove an item from any position in a list, you can use the `pop()` method with an index. For example, let's remove the first item from our list:

```py
{{#include ../../listings/lists/pop.py:pop-index}}
```

which produces the following output:

```txt
{{#include ../../listings/lists/pop.out:4:5}}
```

When used with a positional argument, `pop()` is considerably slower but it gives you more flexibility.

Another method for removing items from a list is `remove()`.
This method is useful when you know the value of the item you want to remove from the list.
The `remove()` method deletes only the first occurrence of the value you specify.
Check this in action:

```py
{{#include ../../listings/lists/remove.py:start}}
```

which gives us:

```txt
{{#include ../../listings/lists/remove.out:1:2}}
```

Notice that only the first `1` is removed from the list.

We can apply `remove()` few more times:

```py
{{#include ../../listings/lists/remove.py:remove-more}}
```

which leaves us with:

```txt
{{#include ../../listings/lists/remove.out:3}}
```

Note that the last `1` is still in the list.

If we try to remove element which is not in the list that would produce an error.

## Clearing a List

If you want to remove everything from a list, you can use the `clear()` method. For example,

```py
{{#include ../../listings/lists/clear.py:all}}
```

which produces:

```py
{{#include ../../listings/lists/clear.out}}
```

## Modifying Elements in a List

It's possible to modify elements in a list by assigning new values to them. Let's see an example:

File: `modify.py`

```py
{{#include ../../listings/lists/modify.py:list}}
```

Here we create a new list of integers and output it to the console:

```txt
{{#include ../../listings/lists/modify.out:1}}
```

We can now update individual elements of the list using assignment operator `=`:

```py
{{#include ../../listings/lists/modify.py:assign}}
```

Note that we update first and last elements of the list. The index-access rules we've seen before apply here as well. The output of the program is:

```txt
{{#include ../../listings/lists/modify.out:2}}
```

It's even possible to modify slices of a list.

```py
{{#include ../../listings/lists/modify.py:slice}}
```

which replaces three middle elements of the list with a single element:

```txt
{{#include ../../listings/lists/modify.out:3}}
```
