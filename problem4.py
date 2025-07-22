from abc import ABC


class Button(ABC):
    def draw(self):
        pass


class ScrollBar(ABC):
    def draw(self):
        pass


class WindowsButton(Button):
    def draw(self):
        print("Windows button")


class WindowsScrollBar(ScrollBar):
    def draw(self):
        print("Windows scrollbar")


class MacButton(Button):
    def draw(self):
        print("Mac button")


class MacScrollBar(ScrollBar):
    def draw(self):
        print("Mac scrollbar")


class LinuxButton(Button):
    def draw(self):
        print("Linux button")


class LinuxScrollBar(ScrollBar):
    def draw(self):
        print("Linux scrollbar")


class UIFactory(ABC):
    def create_button(self):
        pass

    def create_scrollbar(self):
        pass


class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_scrollbar(self):
        return WindowsScrollBar()


class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_scrollbar(self):
        return MacScrollBar()


class LinuxFactory(UIFactory):
    def create_button(self):
        return LinuxButton()

    def create_scrollbar(self):
        return LinuxScrollBar()


def draw_ui(factory: UIFactory):
    button = factory.create_button()
    scrollbar = factory.create_scrollbar()
    button.draw()
    scrollbar.draw()


def main():
    factory = WindowsFactory()
    factory.create_button().draw()
    factory.create_scrollbar().draw()


if __name__ == "__main__":
    main()
