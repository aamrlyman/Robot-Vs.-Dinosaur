import random
from weapon import Weapon

class Dinosaur: 
    

    def __init__(self, name):
        self.name = name
        self.attack_power = random.randrange(20, 60)
        self.health = 20
        self.attacks = [Weapon('Chomp'), Weapon('Tail Whip'), Weapon('Headbut')]
        self.active_attack = self.attacks[1]


    def attack(self, Opponent):
        self.active_attack = self.attacks[int(input('                   Which attack will you want to use? 0 = Chomp, 1 = Tail Whip, 2 = Headbut: '))]
        current_attack_power = int(self.active_attack.attack_power * (random.random()))
        Opponent.health = Opponent.health - current_attack_power
        if Opponent.health < 0:
            Opponent.health = 0
        print (f'Dinosaur {self.name} just did {current_attack_power} hit points of damage to Robot {Opponent.name}.') 
        print(f'Robot {Opponent.name} now has {Opponent.health} hit points left.')
        print('')


