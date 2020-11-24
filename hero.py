import random
from ability import Ability
from armor import Armor
from weapon import Weapon



class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.alive_status = True
        self.deaths = 0
        self.kills = 0

    
    def __str__(self):
        pass
    
    def add_kill(self, num_kills):
        self.kills += num_kills
        
    def add_death(self, num_deaths):
        self.deaths += num_deaths
   
    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
       



        if len(self.abilities) == 0 and len(opponent.abilies) == 0:
            print(f"draw")
        else: #if hero has ability
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                if self.is_alive() == False:
                    print(f"{opponent.name} wins!")
                    self.add_death(1)
                    opponent.add_kill(1)
                elif opponent.is_alive() == False:
                    self.add_kill(1)
                    opponent.add_death(1)
                    print(f"{self.name} wins!")
                    

    
    def add_ability(self, ability):
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
    
    def attack(self):

        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amount):

        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        block_return = damage_amount - total_block
        return block_return

    def take_damage(self, damage):
        # subtracts from current health
        total_dmg = self.defend(damage)
        self.current_health = self.current_health - total_dmg
    
    def is_alive(self):
        #returns true or false depending on current health
        
        if self.current_health <= 0:
            return False
        else:
            return True
         





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())