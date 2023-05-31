# Exercises

## 1. Ask the user for their name and print it to the screen

Python has a built-in function called `input()` that will ask the user for some input.  The function takes a single argument, which is the prompt to display to the user.  The function returns the input as a string.

```py
name = input("What is your name? ")
```

Using `input()`, ask the user for their first and last name. Then print their full name to the screen. Account for the possibility that the user might enter their name in all lowercase letters or use extra spaces before or after their name.

## 2. Ask the user for two numbers and print their sum

Using `input()`, ask the user for two numbers. Convert the strings to flaot and store them in separate variables. Then print the sum of the two numbers.

_Hint: You will need to use the `float()` function to convert the strings to floats._

## 3. Extract username and password from a URL

In Python you can assign multiple variables at once by separating them with commas:

For example, the following statement assigns the value `1` to `x` and the value `2` to `y`:

```py
x, y, _, _ = 1, 2, 3, 4
```

Note that we are using `_` to ignore the last two values.

You can also split a string into multiple variables by using the `split()` method. For example, the following statement assigns the value `'1'` to `x` and the value `'2'` to `y`:

```py
x, y = '1,2'.split(',') # split the string at the comma
```

Using what you have learned, and given the following string:

```py
url = 'postgres://user1:mysecret@localhost:5432/mydb'
```

extract the username and password from the string and print it to the screen.
