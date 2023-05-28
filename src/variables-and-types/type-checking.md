# Type Checking

If you are not sure what type a variable is, you can ask Python to tell you. For example, if you have a variable called `x`, you can ask Python what type it is by using the `type()` function:

```py
{{#include ../../listings/variables-and-types/typechecking.py:type}}
```

which will print:

```txt
{{#include ../../listings/variables-and-types/typechecking.out}}
```

Related to `type()` is the `isinstance()` function, which can be used to check if a variable is of a certain type:

```py
{{#include ../../listings/variables-and-types/typechecking.py:isinstance:1:3}}
```

which will print:

```txt
{{#include ../../listings/variables-and-types/typechecking.out:4:}}
```
