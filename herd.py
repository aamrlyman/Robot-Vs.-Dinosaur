from dinosaur import Dinosaur
from robot import Robot

class Herd:

    def __init__(self):
        self.dinosaur_1 = Dinosaur('Rex')
        self.dinosaur_2 = Dinosaur('TriC')
        self.dinosaur_3 = Dinosaur('Raptor')
        self.herd = [self.dinosaur_1, self.dinosaur_2, self.dinosaur_3]
        
    def herd_attack(self, Opponent):
        counter = 0
        for dino in self.herd:
            dino.attack(Opponent[counter])
            counter +=1

