import random
class Dinosaur: 
    

    def __init__(self, name):
        self.name = name
        self.attack_power = random.randrange(20, 60)
        self.health = 100

    def attack(self, Opponent):
        Opponent.health = Opponent.health - self.attack_power
        print (f'Dinosaur just did {random.randrange(0, self.attack_power)} hit points of damage to Robot {Opponent.name}. Robot {Opponent.name} now has {Opponent.health} hit points left.')
