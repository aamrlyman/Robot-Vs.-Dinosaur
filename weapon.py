import random
class Weapon:

    def __init__(self, name):
    
        self.name = name
        self.attack_power = random.randrange(20, 60)



