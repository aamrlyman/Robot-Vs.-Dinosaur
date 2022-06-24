from dinosaur import Dinosaur
from robot import Robot

class Herd:

    def __init__(self):
        self.dinosaur_1 = Dinosaur('Rex')
        self.dinosaur_2 = Dinosaur('TriC')
        self.dinosaur_3 = Dinosaur('Raptor')
        self.herd = [self.dinosaur_1, self.dinosaur_2, self.dinosaur_3]
        self.total_health = self.dinosaur_1.health + self.dinosaur_2.health + self.dinosaur_3.health

    def herd_attack(self, Opponent):
        selector = 0
        for dino in self.herd:
            
            if dino.health == 0:
                self.herd.remove(dino)
            if Opponent.fleet == []:
                break
            dino.attack(Opponent.fleet[selector])
            selector +=1
            if selector > (len(Opponent.fleet) -1):
                selector = 0
