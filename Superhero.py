class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.energy = 100
    
    def use_power(self):
        if self.energy >= 20:
            print(f"{self.name} uses {self.power}!")
            self.energy -= 20
        else:
            print(f"{self.name} is too tired!")
    
    def rest(self):
        print(f"{self.name} is resting... Zzz")
        self.energy = 100
    
    def status(self):
        print(f"{self.name} - Power: {self.power} - Energy: {self.energy}")

spiderman = Superhero("Spider-woman", "web shooting")
superman = Superhero("Superwoman", "super strength")

spiderman.status()
spiderman.use_power()
spiderman.status()

superman.use_power()
superman.use_power()
superman.use_power()
superman.rest()
superman.use_power() 