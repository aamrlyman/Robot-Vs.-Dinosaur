from dinosaur import Dinosaur
from robot import Robot

t_Rex = Dinosaur('T-Rex')
sam = Robot('Sam')

t_Rex.attack(sam)

sam.attack(t_Rex)
