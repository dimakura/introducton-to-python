# List conditionals

## `in` operator

In [previous section](./complex-conditions.md) we wrote a complex condition which checked if the value of `country` is Cameroon or Malaysia. But what if we have a list of countries? Actually here's a full list of countries with voting age of `21`:

```py
['Cameroon', 'Malaysia', 'Oman', 
 'Samoa', 'Singapore', 'Tokelau',
 'Tonga']
```

We could persue our previous approach and write a complex condition using `or` operator. That would require us to write a lot of code. But there's a better way. We can use the `in` operator to check if a value is in a list. Our program would look like this in such case:

```py
{{#include ../../listings/if-statement/list.py:v3}}
```

which produces:

```txt
{{#include ../../listings/if-statement/list.out:3}}
```

## `not in` operator

We can also check if a value is not in a list using `not in` operator. Here's an example:

```py
{{#include ../../listings/if-statement/list.py:v4}}
```

which indeed tells us:

```txt
{{#include ../../listings/if-statement/list.out:4}}
```

## Check if list is empty

If we want to check if a list is empty we can use the fact that empty lists are considered `False` in Python. Here's an example:

```py
{{#include ../../listings/if-statement/list.py:v5}}
```

This produces:

```txt
{{#include ../../listings/if-statement/list.out:5}}
```

If you add few more cars to the list

```py
{{#include ../../listings/if-statement/list.py:v6}}
```

the output will change to:

```txt
{{#include ../../listings/if-statement/list.out:6}}
```


