# Hello World

Create a new directory called `pyintro` and open it in VS Code.

```sh
$ cd ~          # go to your home directory
$ mkdir pyintro # create a project directory
$ cd pyintro    # change the current directory
$ code .        # open VS Code
```

Create a new file add the following code to it:

File: `hello_world.py`

```py
{{#include ../../listings/getting-started/hello_world.py}}
```

To execute this code, run the following command in the terminal:

```sh
$ conda activate pyintro # make sure you are in the right environment
$ python hello_world.py  # run the script
```

This should print
```txt
{{#include ../../listings/getting-started/hello_world.out}}
```
to the terminal.

Congratulations, you have just written your first Python program!
