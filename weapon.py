import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        # Pick a random value between 0 and self.max_damage
        attack_value = random.randint(int(self.max_damage)//2,int(self.max_damage))
        return attack_value

      