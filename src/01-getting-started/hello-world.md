# Hello World

Create a new directory called `pyintro` and open it in VS Code.

```bash
$ mkdir pyintro # create a project directory
$ cd pyintro    # change the current directory
$ code .        # open VS Code
```

Create a new file called `hello_world.py` and add the following code:

```py
{{#include ../../listings/ch01/hello_world.py}}
```

To execute this code, run the following command in the terminal:

```bash
$ conda activate pyintro # make sure you are in the right environment
$ python hello_world.py  # run the script
```

This should print `Hello, World!` to the terminal.

Congratulations, you have just written your first Python program!
