from abc import ABC, abstractmethod


class Template(ABC):
    def parse(self):
        self.load()
        self.validate()
        self.transform()
        self.export()

    def load(self):
        print("Load")

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    def export(self):
        print("Export")


class CSVParser(Template):
    def validate(self):
        print("Validate CSV")

    def transform(self):
        print("Transform CSV")


class XMLParser(Template):
    def validate(self):
        print("Validate XML")

    def transform(self):
        print("Transform XML")
