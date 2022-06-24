import random
from weapon import Weapon


class Robot:

    def __init__(self, name):

        self.name = name
        self.health = 100
        self.weapons = [Weapon('Plasma Sword'), Weapon('Laser Gun'), Weapon('Grenade')]
        self.active_weapon = self.weapons[1]

    def attack(self, Opponent):
        self.active_weapon = self.weapons[int(input('                   Which weapon you want to use? 0 = Plasma swoard, 1 = Laser Gun, 2 = Grenade: '))]
        Opponent.health = Opponent.health - self.active_weapon.attack_power
        if Opponent.health < 0:
            Opponent.health = 0
        print('')
        print (f'Robot {self.name} just did {random.randrange(0, self.active_weapon.attack_power)} hit points of damage to Dinosaur {Opponent.name}.') 
        print(f'Dinosaur {Opponent.name} now has {Opponent.health} hit points left.')
        print('')