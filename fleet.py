from dinosaur import Dinosaur
from robot import Robot
from herd import Herd

class Fleet:

    def __init__(self):
        self.robot_1 = Robot('Sam')
        self.robot_2 = Robot('Joe')
        self.robot_3 = Robot('Larry')
        self.fleet = [self.robot_1, self.robot_2, self.robot_3]
        self.total_health = self.robot_1.health + self.robot_2.health + self.robot_3.health

    def fleet_attack(self, Opponent):
        selector = 0
        for robot in self.fleet:
            if robot.health == 0:
                self.fleet.remove(robot)
            if Opponent.herd == []:
                break
            robot.attack(Opponent.herd[selector])
            selector +=1
            if selector > (len(Opponent.herd) -1):
                selector = 0
        

