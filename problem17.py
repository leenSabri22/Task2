class Document:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def create_memento(self):
        return Memento(self.shapes)

    def restore_memento(self, memento):
        self.shapes = memento.get_state()

    def show(self):
        return self.shapes


class Memento:
    def __init__(self, state):
        self._state = tuple(state)

    def get_state(self):
        return list(self._state)


class History:
    def __init__(self):
        self._mementos = []

    def save(self, memento):
        self._mementos.append(memento)

    def undo(self):
        if self._mementos:
            return self._mementos.pop()
        return None


if __name__ == "__main__":
    doc = Document()
    history = History()

    doc.add_shape("Circle")
    history.save(doc.create_memento())

    doc.add_shape("Square")
    history.save(doc.create_memento())

    doc.add_shape("Triangle")
    print("Current:", doc.show())

    memento = history.undo()
    if memento:
        doc.restore_memento(memento)
    print("After Undo 1:", doc.show())

    memento = history.undo()
    if memento:
        doc.restore_memento(memento)
    print("After Undo 2:", doc.show())
