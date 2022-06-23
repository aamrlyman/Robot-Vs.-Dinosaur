from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from herd import Herd
from fleet import Fleet

# Battlefield_1 = Battlefield()

# Battlefield_1.run_game()

dinos = Herd()
robots = Fleet()

dinos.herd_attack(robots.fleet)
robots.fleet_attack(dinos.herd)