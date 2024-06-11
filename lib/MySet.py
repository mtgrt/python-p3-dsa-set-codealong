
class MySet:
    def __init__(self, iterable=None):
        self.elements = set()
        if iterable:
            self.elements.update(iterable)

    def add(self, element):
        self.elements.add(element)

    def delete(self, element):
        self.elements.discard(element)

    def has(self, element):
        return element in self.elements

    def size(self):
        return len(self.elements)
