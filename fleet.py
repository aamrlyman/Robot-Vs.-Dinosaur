from dinosaur import Dinosaur
from robot import Robot
from herd import Herd

class Fleet:

    def __init__(self):
        self.robot_1 = Robot('Sam')
        self.robot_2 = Robot('Joe')
        self.robot_3 = Robot('Larry')
        self.fleet = [self.robot_1, self.robot_2, self.robot_3]
        
    def fleet_attack(self, Opponent):
        counter = 0
        for robot in self.fleet:
            robot.attack(Opponent[counter])
            counter +=1
        

