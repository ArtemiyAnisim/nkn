class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f"{self.name} подает голос")

    def move(self):
        print(f"{self.name} дергает хвостом")

class Dog(Animal):
    def __init__(self, name, breed, legs):
        super().__init__(name, breed, legs)
        self.breed = breed

    def bark(self):
        print(f"{self.breed} {self.name} лает")

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species, 2)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.species} {self.name} летaeт")