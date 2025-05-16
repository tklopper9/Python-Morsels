In this exercise, we're going to work on flattening iterables. I'd like you to write a function deep_flatten that accepts a list of lists (or lists of tuples and lists) and returns a flattened version of that list of lists.

It should work like this:

```
deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
[1, 2, 3, 4, 5, 6, 7, 8]

deep_flatten([[1, [2, 3]], 4, 5])
[1, 2, 3, 4, 5]
```

In the examples above, we're returning a list. Your deep_flatten function should return an iterable, not necessarily a list.

Your deep_flatten function can assume that no strings will be passed to it. We'll deal with strings later.