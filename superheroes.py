import random

class Ability:
    def __init__(self, name:str, max_damage:int):
        self.name = name
        self.max_damage = max_damage

    
    def attack(self):
        attack = random.randint(0, self.max_damage)
        return attack




class Armor:
    def __init__(self, name:str, max_block:int):
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block



class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        damage = 0 
        for abilities in self.abilities:
            damage += abilities.attack()
        return damage

    def add_armor(self, damage_amt):
        damage_amt = 0
        for hero in self.armors:
            damage_amt += hero.block()
        return damage_amt
        

    def take_damage(self, damage):
        self.current_health -= damage
        

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def add_kills(self, num_kills=1):
        self.kills += num_kills

    def add_deaths(self, num_deaths=1):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def fight(self, opponent):
        hero = random.randint(0, 1)
        rounds = 0
        while self.is_alive() and opponent.is_alive() and rounds < 200:
            if hero == 0:
                damage = self.attack()
                print(damage)
                opponent.take_damage(damage)
                hero = 0
            else:
                damage = opponent.attack()
                print(damage)
                self.take_damage(damage)
                hero = 0
            print('{}: {} HP | {}: {} HP'.format(self.name, self.current_health, opponent.name, opponent.current_health))
        
        if (self.is_alive()):
            self.add_kills()
            opponent.add_deaths()
            print(self.name + ' Won the brawl!')
        elif (opponent.is_alive()):
            self.add_deaths()
            opponent.add_kills()
            print(opponent.name + ' Won the brawl!')
        else: 
            print("Draw!")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.ability(ability1)
    hero1.ability(ability2)
    hero2.ability(ability3)
    hero2.ability(ability4)
    hero1.fight(hero2)