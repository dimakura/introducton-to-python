# Strings

In previous section we declared a string variable `message` and printed it to the screen. 

```py
{{#include ../../listings/ch02/hello_world_typed.py:all}}
```

What exactly is a string? A string is a sequence of characters. In the example above, the string `"Hello, World!"` consists of 13 characters: `H`, `e`, `l`, `l`, `o`, `,`, ` `, `W`, `o`, `r`, `l`, `d`, `!`.

Strings are one of the most common data types that you'll encounter in Python programs. You can use them to represent names, addresses, messages, and many other kinds of information.

Strings are easy to recognize in Python programs. They are enclosed in single or double quotes. In previous example we used double quotes, but single quotes are also valid:

```py
{{#include ../../listings/ch02/message_comparison.py}}
```

Both declarations are equivalent.

You can use either single or double quotes, but you should be consistent. If you start a string with a single quote, you should end it with a single quote. If you start it with a double quote, you should end it with a double quote.

It's possible to use single quotes inside a string that is enclosed in double quotes, and vice versa. For instance this program

```py
{{#include ../../listings/ch02/quoted_strings.py}}
```

produces the following output:

```txt
{{#include ../../listings/ch02/quoted_strings.out}}
```

It's also possible to use the same type of quotes inside a string, but you have to escape them with a backslash `\`, for instance:

```py
"I said, \"Hello, World!\""
```

## Some Useful String Methods

Python provides a number of useful methods for working with strings. A method is an action that Python can perform on a piece of data. The dot `.` after the name of the variable `name` in the following example tells Python to make the `upper()` method act on the variable.

```py
{{#include ../../listings/ch02/upper_method.py}}
```

This program produces the following output:

```txt
{{#include ../../listings/ch02/upper_method.out}}
```

Similarly, the `lower()` method changes a string to all lowercase:

```py
{{#include ../../listings/ch02/lower_method.py}}
```

with output

```txt
{{#include ../../listings/ch02/lower_method.out}}
```

One more method, which we'll use a lot in this book, is `title()`.
It changes each word to title case, where each word begins with a capital letter:

```py
{{#include ../../listings/ch02/title_method.py}}
```

which produces the following output:

```txt
{{#include ../../listings/ch02/title_method.out}}
```

## String Formatting

Very often you'll want to combine several strings, for example if you have `first_name` and `last_name` variables, you might want to combine them into a single string `full_name`. Python provides several ways to do this. In this section we'll look at the `f-string` method.

Look at the following example:

```py
{{#include ../../listings/ch02/f_strings.py}}
```

and its output:

```txt
{{#include ../../listings/ch02/f_strings.out}}
```

First two lines should be familiar to you, we declare two string variables
for first and last names. The third line is more interesting

```py
{{#include ../../listings/ch02/f_strings.py:3}}
```

Here, we initialize variable with an _f-string_. The _f_ stands for _format_.
An f-string is a string that has an `f` at the beginning and curly braces `{}` containing expressions that will be replaced with their values.

We can place any valid Python expression inside the curly braces. For example, we can use the `title()` method to titleize a string:

```py
{{#include ../../listings/ch02/f_strings2.py}}
```

which outputs a nicely formatted greeting:

```txt
{{#include ../../listings/ch02/f_strings2.out}}
```

## Dealing with Whitespaces

Whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it's easier for users to read.

A table below lists some of the whitespace characters:

| Name    | Character |
| ------- | --------- |
| Space   | `' '`     |
| Tab     | `'\t'`    |
| Newline | `'\n'`    |

And here's an example of using tabs and newlines:

```py
{{#include ../../listings/ch02/whitespace.py}}
```

and its output:

```txt
{{#include ../../listings/ch02/whitespace.out}}
```

Quite often you'll want to strip whitespace from strings. For example, you might want to remove extra whitespace from the right side of a name before storing it. Python provides a number of methods for stripping whitespace from strings.

The basic methods for removing excess whitespace are `rstrip()`, `lstrip()`, and `strip()`. The `lstrip()` method removes whitespace from the left side of a string, `rstrip()` removes whitespace from the right side, and `strip()` removes whitespace from both sides.

Try to run the following program:

```py
{{#include ../../listings/ch02/strip.py}}
```

and compare the output:

```txt
{{#include ../../listings/ch02/strip.out}}
```

## Removing Prefixes

Another useful method is `removeprefix()`. It removes a prefix from a string. For example, if you have an url, you can remove ``

```py
{{#include ../../listings/ch02/removeprefix.py}}
```

which produces the following output:

```txt
{{#include ../../listings/ch02/removeprefix.out}}
```
