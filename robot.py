import random
from weapon import Weapon


class Robot:

    def __init__(self, name):

        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Plasma Sword')

    def attack(self, Opponent):
        Opponent.health = Opponent.health - self.active_weapon.attack_power
        print (f'Robot {self.name} just did {random.randrange(0, self.active_weapon.attack_power)} hit points of damage to Dinosaur {Opponent.name}. Dinosaur {Opponent.name} now has {Opponent.health} hit points left.')
    