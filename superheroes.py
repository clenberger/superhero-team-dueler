import random

class Ability:
    def __init__(self, name:str, max_damage:int):
        self.name = name
        self.max_damage = max_damage

    
    def attack(self):
        attack = random.randint(0, self.max_damage)
        return attack




# class Armor:
#     def __init__(self, name:str, max_block:int):
#         self.name = name
#         self.max_block = max_block

#     def block():
    


# class Hero:
#     def __init__(self, name:str, starting_health=100):
#         self.name = name
#         self.starting_health = starting_health

#     def ability(Ability):
        

#     def attack():
        

#     def defend(incoming_damage:int):
        

#     def take_damage(damage):
        

#     def is_alive():
        

#     def fight():
        

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())