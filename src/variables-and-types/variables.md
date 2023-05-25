# Variables

In the previous lecture we wrote a simple program that printed a message to the screen.

Here's an equivalent program:

File: `hello-world.py`

```py
{{#include ../../listings/ch02/hello_world.py:all}}
```

We can run this program by typing `python hello-world.py` in the terminal. As before, the program will print the message `"Hello, World!"` to the screen.

> **Note**: Miniconda environment, `pyintro`, should be activated before running the program.
>
> ```bash
> $ conda activate pyintro
> ```
>
> This will be our default way of running Python programs in this book.
> And we won't remind you about it in the future.

Back to the program. The first line of the program declares a variable.

```py
{{#include ../../listings/ch02/hello_world.py:var}}
```

In Python, variables are created when you assign a value to them using the `=` operator. In this case, we assign the message `"Hello, World!"` to the variable `message`.

Variable has a name and a value. In this case, the name of the variable is `message` and the value is `"Hello, World!"`. You can think of variables as containers for storing data. We can later use the variable to access the data stored in it, by its name. Like we do on the second line:

```py
{{#include ../../listings/ch02/hello_world.py:print}}
```

## Type annotation

One important propery of a variable, which might not be obvious from the example above, is its _type_. In this case, the type of the variable is `str`, which is short for _string_. To make this more explicit, we could have declared the variable in the following way:

```py
{{#include ../../listings/ch02/hello_world_typed.py:var}}
```

(note the `: str` part after variable name).

This is called _type annotation_. It is not necessary in this case, because Python can infer the type of the variable from the value assigned to it. However, it is a good practice to use type annotations in your programs.

In the rest of the book, we will use type annotations in all examples. Though, you can omit them at the beginning, if you find them confusing.

The rest of the program is the same as before:

```py
{{#include ../../listings/ch02/hello_world_typed.py:all}}
```

with the same output

```txt
{{#include ../../listings/ch02/hello_world_typed.out}}
```

> ### Exercise
>
> Try to change the program above a bit further.
> Declare a variable `name` and assign your name to it, for example `"Bill"`.
> Then print a message that says `"Hello, Bill!"`, using the `name` variable.
> In the next section you'll learn how to write such a program, but try to figure it out yourself first.
