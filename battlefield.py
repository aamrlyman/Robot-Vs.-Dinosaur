from robot import Robot
from dinosaur import Dinosaur 
from herd import Herd
from fleet import Fleet 
import random 

class Battlefield:

    def __init__(self):
        self.robots = Fleet()
        self.dinos = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print('')
        print(f'Welcome to the an epic battle for the ages: The fight between the Robots and the Dinosaurs.')
        print("Only one team can win!")
        print('')

    def battle_phase(self):
            teams = ['Dinosaurs', 'Robots']
            first_strike = random.choice(teams)
            
            if first_strike == 'Dinosaurs':
                print('The Dinosaurs won first strike!')
                while self.robots.total_health > 0 and self.dinos.total_health > 0:
                    self.dinos.herd_attack(self.robots)
                    if self.robots.fleet ==[]:
                        break
                    self.robots.fleet_attack(self.dinos)
                    if self.dinos.herd ==[]:
                        break
            else:
                print('The Robots won first strike!')
                while self.robots.total_health > 0 and self.dinos.total_health > 0:
                    self.robots.fleet_attack(self.dinos)
                    if self.dinos.herd ==[]:
                        break
                    self.dinos.herd_attack(self.robots)
                    if self.robots.fleet ==[]:
                        break
    def display_winner(self):
        if self.dinos.herd == []:
            print('The Robots triumphed over the Dinosaurs!!')
        else:
            print('The Dinosaurs triumphed over the Robots!!')

        


