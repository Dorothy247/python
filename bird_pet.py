class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.species = "bird"

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} pecks at some seeds happily!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} tucks its head under its wing and sleeps.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} flutters around and plays with a toy!")
        else:
            print(f"{self.name} is too tired to play right now.")

    def sing(self):
        if self.happiness >= 3:
            print(f"{self.name} chirps a beautiful melody!")
            self.happiness = min(10, self.happiness + 1)
        else:
            print(f"{self.name} doesn't feel like singing right now.")

    def fly(self):
        if self.energy >= 3:
            self.energy -= 3
            self.hunger = min(10, self.hunger + 2)
            print(f"{self.name} takes off and flies around the room!")
        else:
            print(f"{self.name} is too tired to fly right now.")

    def train(self, trick):
        if self.energy >= 2 and self.happiness >= 4:
            self.tricks.append(trick)
            self.energy -= 2
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned to {trick}!")
        else:
            print(f"{self.name} isn't in the right mood to learn tricks now.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n{self.name} the {self.species}'s status:")
        print(f"Hunger: {'▣' * (10 - self.hunger)}{'□' * self.hunger} ({self.hunger}/10)")
        print(f"Energy: {'▣' * self.energy}{'□' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'▣' * self.happiness}{'□' * (10 - self.happiness)} ({self.happiness}/10)")