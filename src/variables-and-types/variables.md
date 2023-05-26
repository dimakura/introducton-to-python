# Variables

In the [previous chapter](../getting-started/hello-world.md) we wrote a simple program that printed a welcome message to the screen.

Now we'll rewrite this program using variables.

File: `hello-world.py`

```py
{{#include ../../listings/variables-and-types/hello_world.py:start}}
```

As before, we can run this program by typing,

```sh
$ python hello-world.py
```

in the shell. As before, the program will print the message

```txt
{{#include ../../listings/variables-and-types/hello_world.out:1}}
```

to the screen.

> **Note**: The conda environment, `pyintro`, should be activated before running the program.
>
> ```sh
> $ conda activate pyintro
> $ python hello-world.py
> ```
>
> This will be our way of running Python programs in this book. And we won't remind you about it in the future.

So if the program does the same thing as before, what's the point of writing it in a different way? Before we answer this question, let's take a closer look at the program.

The first line of the program declares a variable:

```py
{{#include ../../listings/variables-and-types/hello_world.py:var}}
```

In Python, variables are created when you assign a value to them using the `=` operator. Variable has a name and a value. In our case, the name of the variable is `message` and the value we assign to it is `"Hello, World!"`.

You can think of variables as containers for storing data. We can later use the variable to access the data stored in it, by its name. In our case, we used the variable `message` to print the message to the screen:

```py
{{#include ../../listings/variables-and-types/hello_world.py:print}}
```

The nice thing about variables is that we can continue to use them in other parts of the program. For example, we can print the message again, but this time printing it with uppercase letters. For this, we can add a new line to the program:

```py
{{#include ../../listings/variables-and-types/hello_world.py:print2}}
```

The output of the program will be

```txt
{{#include ../../listings/variables-and-types/hello_world.out:1:2}}
```

To answer our question from the beginning of this section, the point of using variables is that they allow us to reuse the data stored in them. In our case, we stored the message in the variable `message` and then used it twice in the program. If we need to change the message, we only need to change it in one place, where we assign the value to the variable. The rest of the program will use the new value automatically.

## Type Hits

One important propery of a variable, which might not be obvious from the example above, is its _type_. In this case, the type of the variable is `str`, which is short for _string_. To make this more explicit, we could have declared the variable in the following way:

```py
{{#include ../../listings/variables-and-types/hello_world.py:typed-var}}
```

(note the `: str` part after variable name).

This is called _type hint_. Python is a dynamically typed language, which means that you don't have to specify the type of the variable when you declare it. And, event if you do, Python will ignore it. However, it is a good practice to do so, because it makes the code easier to read and understand. Also different tools can use type hints to provide additional help when writing the code.

In the rest of the book, we will use type hints in almost all examples. Though, you can omit them at the beginning, if you find them confusing.

The rest of the program is the same as before:

```py
{{#include ../../listings/variables-and-types/hello_world.py:typed}}
```

with the same output

```txt
{{#include ../../listings/variables-and-types/hello_world.out:3}}
```
