class Character:
    def __init__(self, font, size):
        self.font = font
        self.size = size

    def write_char(self, char, pos):
        print(
            f"write '{char}' with font {self.font}, size {self.size}, at position {pos}"
        )


class CharacterFactory:
    _cache = {}

    @classmethod
    def get_character(cls, font, size):
        key = (font, size)
        if key not in cls._cache:
            cls._cache[key] = Character(font, size)
        return cls._cache[key]


print("new branch")
