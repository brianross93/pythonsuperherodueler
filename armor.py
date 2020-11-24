#Create a new class called Armor that contains two methods: __init__ and block.
#The block method should return an integer between 0 and the max_block strength.

import random

class Armor:
    def __init__(self, name, max_block):

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_block = max_block

    def block(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''

      # Pick a random value between 0 and self.max_damage
      block_value = random.randint(0,int(self.max_block))
      return block_value

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    block = Armor("Cloth", 20)
    print(block.name)
    print(block.block())