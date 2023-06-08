# Dictionaries

Dictionary is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.

## Creating a Dictionary

To define a dictionary, you use curly braces `{}` to indicate the beginning and end of the dictionary, and use `:` to separate keys and values. A simple dictionary looks like this:

```python
{{#include ../../listings/collections/dictionaries.py:dict}}
```

which produces the following output:

```text
{{#include ../../listings/collections/dictionaries.out:1}}
```

Note that after Python 3.6, the order of the key-value pairs is preserved. In earlier versions of Python, the order of the key-value pairs is not preserved.

Also note that the keys in a dictionary must be unique. If you use the same key twice, the second key-value pair will overwrite the first one.

## Accessing Values

To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets `[]`. For example, the following snippet

```python
{{#include ../../listings/collections/dictionaries.py:dict_access}}
```

produces an output:

```text
{{#include ../../listings/collections/dictionaries.out:2:5}}
```

If we try to access a key that doesn't exist in a dictionary

```python
{{#include ../../listings/collections/dictionaries.py:dict_error}}
```

Python will raise an error:

```text
{{#include ../../listings/collections/dictionaries.out:13:17}}
```

If this is an issue, there's another way to access a value in a dictionary. The `get()` method returns `None` if the key doesn't exist in the dictionary. You can also specify a default value to use if the key doesn't exist.

```python
{{#include ../../listings/collections/dictionaries.py:dict_get}}
```

If you need to check whether dictionary has a particular key, you can use the `in` operator.

```python
{{#include ../../listings/collections/dictionaries.py:dict_in}}
```

## Looping Through a Dictionary

It's very common to loop through all key-value pairs in a dictionary.

Below is an example of using `for` loop. Notice that the `language` variable gets the successive keys in the dictionary as the loop moves through the dictionary.

```python
{{#include ../../listings/collections/dictionary_loop.py:dict_loop}}
```

And this the output:

```text
{{#include ../../listings/collections/dictionary_loop.out:1:4}}
```

Because it's common to use both key and value of a dictionary while looping through it, Python provides a special method called `items()` that returns a list of key-value pairs. In the following example, we use `items()` to loop through the dictionary and do the same thing as the previous example.

```python
{{#include ../../listings/collections/dictionary_loop.py:dict_items}}
```

The `keys()` method returns a list of all keys in a dictionary. The `values()` method returns a list of all values in a dictionary. These two methods can be used in variour ways. For example, you can loop through keys in sorted order:

```python
{{#include ../../listings/collections/dictionary_loop.py:dict_sorted_keys}}
```

Which produces almost the same output as the previous examples, except that the languages are now sorted:

```text
{{#include ../../listings/collections/dictionary_loop.out:9:12}}
```

## Change Dictionaries

It's fairly easy to change dictionaries. You can add new key-value pairs, modify existing key-value pairs, and remove key-value pairs.

The following example creates an empty dictionary and adds key-value pairs to it. In tnis case we add names of students as keys and their yearly points as values.

```python
{{#include ../../listings/collections/dictionary_change.py:dict}}
```

Another way to add or change key-value pairs in a dictionary is to use the `update()` method. The `update()` method takes a dictionary as an argument and adds all key-value pairs from that dictionary to the current dictionary. If the key already exists, the value associated with that key is replaced.

```python
{{#include ../../listings/collections/dictionary_change.py:dict_update}}
```

If we print `students` dictionary now, we'll see that the argument dictionary was added to the `students` dictionary.

```text
{{#include ../../listings/collections/dictionary_change.out:1}}
```

If we need to remove items from a dictionary, there are few ways to do it. The `popitem()` mehtod removes the last key-value pair from a dictionary and returns it as a tuple.

```python
{{#include ../../listings/collections/dictionary_change.py:dict_popitem}}
# => {{#include ../../listings/collections/dictionary_change.out:2}}
```

The `pop()` method removes a key-value pair from a dictionary and returns the value associated with the key. If the key doesn't exist, the method returns the default value specified as the second argument (or fails with error).

```python
{{#include ../../listings/collections/dictionary_change.py:dict_pop}}
```

The `del` statement removes a key-value pair from a dictionary.

```python
{{#include ../../listings/collections/dictionary_change.py:dict_del}}
```

And, finally, the `clear()` method removes all key-value pairs from a dictionary.

