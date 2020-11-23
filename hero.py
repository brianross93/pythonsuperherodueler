import random





class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def __str__(self):
        pass
    
    def fight(self, opponent):
        
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        #1) randomly choose winner,
        #Hint: Look into random library, more specifically the choice method
        fightwinner = random.choice([self, opponent])
        print(fightwinner.name)
        return fightwinner



if __name__ == "__main__":
    hero1 = Hero("Marty Martian")
    hero2 = Hero("Henry Hammer")

    hero1.fight(hero2)
    