from collections.abc import Iterable

def deep_flatten(input):
    for item in input:
        if isinstance(item, Iterable) and not isinstance(item, str):
            yield from deep_flatten(item)
        else:
            yield item