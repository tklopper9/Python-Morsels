class OrderedSet():
    def __init__(self, iterator):
        self.items = []
        self.set_items = set()
        if iterator:
            for item in iterator:
                self.add(item)
    def add(self, item):
        if item not in self.set_items:
            self.items.append(item)
            self.set_items.add(item)
    def discard(self, item):
        if item in self.set_items:
            self.set_items.remove(item)
            self.items.remove(item)
    def __len__(self):
        return len(self.set_items)
    def __iter__(self):
        for item in self.items:
            yield item
    def __contains__(self, item):
        return item in self.set_items
    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.items == other.items
        if isinstance(other, set):
            return self.set_items == other
        return False