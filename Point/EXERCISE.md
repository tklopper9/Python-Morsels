I'd like you to write a class representing a 3-dimensional point.

The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes. It must also have a helpful string representation. Additionally, point objects should be comparable to each other (two points are equal if their coordinates are the same and not equal otherwise).

Example usage:

```
p1 = Point(1, 2, 3)

p1
Point(x=1, y=2, z=3)

p2 = Point(1, 2, 3)

p1 == p2
True

p2.x = 4

p1 == p2
False

p2
Point(x=4, y=2, z=3)
```

If you finish the base exercise quickly, consider working through a bonus or two.