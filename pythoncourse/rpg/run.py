from game import Person
from magic import Magic

print("This is the instruction")
#magic
fire =Magic("fire",10,30,"dark")
wind =Magic("wind",15,50,"dark")
ice =Magic("Ice",20,70,"dark")
 player = Person ("Daniel",500,100,50)
 enemy =Person("Vampire",1000,100,20)

 player.stats()
 enemy.stats()

 running =True
 while running:
     print(player.name)
     print("choose your action")
     player.choose_action()
try:

     choice =int(intput(">>>":"))
 except ValueError:
     print("choose a number")
     continue
     action_index= choice -1
    if action_index ==0:
        damage =player.generate_atk_damage()
        enemy.take_damage(damage)
        print("you attacked { } and dealt {} damage".format(enemy.name,damage))

    if action_index ==1:
        player.choose_magic()
        magic_choice =int (input">>>")

    else:
       print("Choose a correct number")
       continue

# ENEMY'S TURN
   enemy_choice = 0
   if enemy_choice == 0:
       enemy_damage = enemy.generate_atk_damage()
       player.take_damage(enemy_damage)

       print("{} attacked {} and dealt {} damage".format[enemy.name, player.name, enemy_damage ])


       player.stats()
       enemy.stats()

       if player.hp == 0:
           print("You lost")
           running = False
       if enemy.hp == 0
           print("You won")
           running = Falseelse:
       print("Choose a correct number")
       continue
