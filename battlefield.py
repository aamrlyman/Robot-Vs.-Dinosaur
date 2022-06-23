from robot import Robot
from dinosaur import Dinosaur 
import random 

class Battlefield:

    def __init__(self):
        self.robot = Robot('Sam')
        self.dinosaur = Dinosaur('Rex')

    def run_game(self):
        battle = Battlefield()
        battle.display_welcome()
        battle.battle_phase()
        battle.display_winner()


    def display_welcome(self):
        print(f'Welcome to the an epic battle for the ages: The fight between {self.robot.name} the Robot and {self.dinosaur.name} the Dinosaur.')
        print("Only one can win!")
        print('')

    def battle_phase(self):
            while self.robot.health > 0 and self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
                if self.robot.health == 0:
                    break
                self.robot.attack(self.dinosaur)
    
    def display_winner(self):
        if self.robot.health > self.dinosaur.health:
            print(f'Robot {self.robot.name} triumphed over dinosaur {self.dinosaur.name}!!')
        else:
            print(f'Dinosaur {self.dinosaur.name} triumphed over Robot {self.robot.name}!!')

        


