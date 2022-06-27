import random
from weapon import Weapon

class Dinosaur: 
    

    def __init__(self, name):
        self.name = name
        self.attack_power = random.randrange(20, 60)
        self.health = 100
        self.attacks = [Weapon('Chomp'), Weapon('Tail Whip'), Weapon('Headbut')]
        self.active_attack = self.attacks[1]


    def attack(self, Opponent):
        Opponent.health = Opponent.health - self.attack_power
        if Opponent.health < 0:
            Opponent.health = 0
        self.active_attack = self.attacks[int(input('                   Which attack will you want to use? 0 = Chomp, 1 = Tail Whip, 2 = Headbut: '))]
        Opponent.health = Opponent.health - self.active_attack.attack_power
        print (f'Dinosaur {self.name} just did {random.randrange(0, self.attack_power)} hit points of damage to Robot {Opponent.name}.') 
        print(f'Robot {Opponent.name} now has {Opponent.health} hit points left.')
        print('')


