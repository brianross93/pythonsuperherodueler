import random


class Team:
    
    
    #__init__: Parameters: name: String
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    #add_hero: Parameters: hero:String

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)
        

    #remove_hero: Parameters name: String

    def remove_hero(self, name):
        foundHero = False
    # loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
            foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    #view_all_heroes: Parameters: None
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)
    
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            fighting_hero = random.choice(living_heroes)
            fighting_opponent = random.choice(living_opponents)
            fighting_hero.fight(fighting_opponent)
            if fighting_hero.is_alive():
                living_opponents.remove(fighting_opponent)
            elif fighting_opponent.is_alive():
                living_heroes.remove(fighting_hero)
            else: 
                living_heroes.remove(fighting_hero)
                living_opponents.remove(fighting_opponent)


