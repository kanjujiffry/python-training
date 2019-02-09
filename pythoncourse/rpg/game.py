
import random #used to generate random number for an attack hp
class Person ():class Person:
   def __init__(self, name, hp, mp, atk):
       self.maxhp = hp  # HP of character when it's full
       self.hp = hp    # HP during the game will change, but the max HP should stay the same
       self.maxmp = mp  # Same like HP
       self.mp = mp
       self.atk_high = atk + 10
       self.atk_low = atk - 10
       self.action = ["Physical Attack"]
       self.name = name

   def stats(self):
       print(self.name)
       print(f"{self.hp}/{self.maxhp}")
       pritn(f"{self.mp}/{self.maxmp}")

   def generate_atk_damage(self):
       dmg = random.randint (self.atk_low, self.atk_high) #this function will return a random number
       return dmg

   def take_damage(self, dmg):
       self.hp = self.hp - dmg
       if self.hp < 0:
           self.hp = 0
       return self.hp

   def choose_action(self):
       index = 1
       print("ACTIONS: ")
       for element in self.action:
           print("{}, {}".format(index, element))
           index = index + 1
