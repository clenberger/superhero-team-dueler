import random
#Massive thank you to Alex Gray for helping me with everything. I completely redid my project after some complications with my code quality and he walked me through everything.
# Ability class
class Ability:
    def __init__(self, name:str, max_damage:int):
        self.name = name
        self.max_damage = max_damage

    
    def attack(self):
        attack = random.randint(0, self.max_damage)
        return attack



# Armor class
class Armor:
    def __init__(self, name:str, max_block:int):
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block



# Hero Class
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
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
            print(self.name + ' won this round!!!')
        elif (opponent.is_alive()):
            self.add_deaths()
            opponent.add_kills()
            print(opponent.name + ' won this round!!')
        else: 
            print("Draw!")



# Weapon Class
class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)    



# Team Class
class Team:
    def __init__ (self, name):
        self.name = name
        self.heroes = []

    def remove_hero (self, name):
        for hero in self.heroes:     
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        while self.heroes and other_team.heroes:
            hero_1 = random.choice(self.heroes)
            hero_2 = random.choice(other_team.heroes)
            if hero_1.is_alive() and hero_2.is_alive():
                hero_1.fight(hero_2)
            
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            ratio = hero.kills / hero.deaths
            print(hero.name + "'s ratio is: " + ratio)




# Tests
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Batman")
    hero2 = Hero("Iron Man")
    ability1 = Ability("Speed", 300)
    ability2 = Ability("Agility", 130)
    ability3 = Ability("Lasers", 100)
    ability4 = Ability("Nokia-like armor", 200)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)