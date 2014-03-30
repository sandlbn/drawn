
class Cart:
    elements = []
    def ___init__(self):
        self.i = -1

    def __iter__():
        return self

    def next(self):
        if self.i<len(self.elements):
            self.i += 1
            return self.elements[self.i]
        else:
            raise StopIteration

    def add(self, element):
        self.elements.append(element)

