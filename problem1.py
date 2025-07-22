class Animal:
    def speak(self):
        pass

    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Dog says: Woof!"

    def move(self):
        return "Dog runs in the yard."


class Cat(Animal):
    def speak(self):
        return "Cat says: Meow!"

    def move(self):
        return "Cat climbs the tree."


class Bird(Animal):
    def speak(self):
        return "Bird says: Tweet!"

    def move(self):
        return "Bird flies in the sky."


class Fish(Animal):
    def speak(self):
        return "Fish says: Blub!"

    def move(self):
        return "Fish swims in the tank."


class UnknownAnimal(Animal):
    def speak(self):
        return "Unknown animal sound."

    def move(self):
        return "Unknown movement."


class Factory:
    @staticmethod
    def create_animal(type):
        type = type.lower()
        if type == "dog":
            return Dog()
        elif type == "cat":
            return Cat()
        elif type == "bird":
            return Bird()
        elif type == "fish":
            return Fish()
        else:
            return UnknownAnimal()


def main():
    animal = Factory.create_animal(input("Enter an animal (dog/cat/bird/fish) "))
    print(animal.speak())
    print(animal.move())


if __name__ == "__main__":
    main()
