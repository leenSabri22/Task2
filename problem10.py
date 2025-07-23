from abc import ABC, abstractmethod


# command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Document:
    def __init__(self):
        self.text = ""

    def type_text(self, new_text):
        self.text += new_text

    def delete_text(self):
        deleted_text = self.text[-1:]
        self.text = self.text[:-1]
        return deleted_text

    def __str__(self):
        return self.text


class TypeCommand(Command):
    def __init__(self, doc, text):
        self.doc = doc
        self.text = text

    def execute(self):
        self.doc.type_text(self.text)

    def undo(self):
        self.doc.delete_text(len(self.text))


class DeleteCommand(Command):
    def __init__(self, doc, count=1):
        self.doc = doc
        self.count = count
        self.deleted_text = ""

    def execute(self):
        self.deleted_text = self.doc.delete_text(self.count)

    def undo(self):
        self.doc.type_text(self.deleted_text)


class MacroCommand(Command):
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def execute(self):
        for cmd in self.commands:
            cmd.execute()

    def undo(self):
        for cmd in reversed(self.commands):
            cmd.undo()


class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
