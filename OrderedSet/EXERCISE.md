### Problem Statement

I'd like you to make an OrderedSet class. This class should work like a set, but it should also maintain the insertion order of the items added to it (unlike Python's built-in set which is unordered).

```
ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']

print(*set(ordered_words))
in these words an order are

print(*OrderedSet(ordered_words))
these are words in an order

print(*OrderedSet(['repeated', 'words', 'are', 'not', 'repeated']))
repeated words are not
```

This set should be relatively memory efficient and containment checks should be relatively time efficient:

```
words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])

len(words)
4

'hello' in words
True
```