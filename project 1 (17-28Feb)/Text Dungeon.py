import time
import sys


#intro
print("Welcome to Text Dungeon!\n\nInstructions: type exactly what is between quotation marks to make your choice.")

while input("Type \"start\" to begin.\n> ") != "start": 
    print("\nInvalid input, please enter \"start\"")

#entering the dungeon
print("\n\nYou seek to enter this dark dungeon in the search of fame and riches.")
while input("Type \"enter\" to enter the dungeon.\n> ") != "enter":
    print("\nInvalid input, please enter \"enter\"")
    
#choice up or down
print("\n\nYou enter the dungeon and you come across a big spiral staircase.")
choice_stairs = ""
while choice_stairs != "up" or choice_stairs != "down":
    print("Do you go \"up\" or \"down\"?")
    choice_stairs = input("> ")
    if choice_stairs == "up":
        print("\n\nYou go up and see that the wals and ceiling have collapsed, blocking your path.\nYou decide to go down the stairs.")
        time.sleep(4)
        print("\nYou go all the way down the spiral staircase which brings you to a giant door.\nYou open the door and find yourself in an armory with all kinds of different weapons.")
        break
    elif choice_stairs == "down":
        print("\n\nYou go all the way down the spiral staircase which brings you to a giant door.\nYou open the door and find yourself in an armory with all kinds of different weapons.")
        break
    else:
        print("\nInvalid input, please enter \"up\" or \"down\".\n")
        continue

#choice great axe or spear
choice_weapon = "" 

while choice_weapon != "up" or choice_weapon != "down":
    print("\nDo you replace your old rusty sword with a cleaving \"great axe\" or an armour piercing \"spear\"?")
    choice_weapon = input("> ")
    
    if choice_weapon == "great axe":
        print("\nYou pickup the great axe.")
        break
    elif choice_weapon == "spear":
        print("\nYou pickup the spear.")
        break
    else:
        print("\nInvalid input, please enter \"great axe\" or \"spear\".")
        continue

#choice big spike pit
time.sleep(2)
print("\n\nYou exit the armory through a second door on the other side of the armory leading deeper into the dungeon."
      "\nAfter walking through a long straight corridor you come across a big spike pit which is blocking your way.\n")
choice_pit = ""

while choice_pit != "wallrun" or choice_pit != "jump":
    print("Do you try to \"wallrun\" or \"jump\" to get to the other side of the pit?")
    choice_pit = input("> ")
    
    if choice_pit == "wallrun":
        print("\nYou run up the wall, but this old dungeon had accumulated a lot of moss on his walls."
              "\nYou slip and plummet down into the big spike pit meeting a swift death.\n"
              "GAME OVER")
        sys.exit()
    elif choice_pit == "jump":
        print("\nYou take a run-up and jump. While in the air you can see that you are not able to make the jump,"
              "instead you can only barely grab the edge of the pit and pull yourself up.")
        break
    else:
        print("\nInvalid input, please enter \"wallrun\" or \"jump\".")
        continue
 
#choice boss   
time.sleep(2)
print("\nYou walk deeper into the dungeon and come across two doors. One door had a symbol with a big armoured monster."
      "The other door had a symbol of a necromancy with an army of skeletons. You remember which weapon you chose.\n")
choice_boss = ""

while choice_boss != "monster" or choice_boss != "necromancer":
    print("Which door do you choose? \"monster\" or \"necromancer\"")
    choice_boss = input("> ")
    
    #necromancer path
    if choice_boss == "necromancer":
        print("\nYou walk up to the door and you see that you have a riddle to solve.")
        time.sleep(2)
        riddle_answer_necro = ""
       
        while riddle_answer_necro != "33":
            print("\nThe riddle is as follows:\n\n2, 3, 5, 9, 17, _\nWhat is the next number in the sequence?")
            riddle_answer_necro = input("> ")
           
            if riddle_answer_necro == "33": 
                print("\nCorrect!")
                time.sleep(2)
                print("\n\nThe door opens and you are in a big room full of treasure chests!\n"
                      "Suddenly a dark mist envelops you. You can't see anything.\n"
                      "When the mist disperses, a necromancer stand before you, ready to defend his treasure.\n")
                fight_necro = ""
               
                while fight_necro != "fight":
                    print("Enter \"fight\" to begin the fight.")
                    fight_necro = input("> ")
                    
                    if fight_necro == "fight":
                       if choice_weapon == "great axe":
                            print("\nYour great axe completely annihilates the skeleton army. They are no match for\n"
                                  "your great axe. The necromancer is the only one left.\n"
                                  "You charge at the necromancer en kill him with one final blow. You loot\n"
                                  "the room and leave. Fame and riches are now yours!\n\nYOU WIN")
                            sys.exit()
                       else:
                            print("\nYour spear isn't made for fighting a lot of targets simultaneously.\n"
                                  "You get overrun by the sheer amount of skeletons.\n\nGAME OVER ")
                            sys.exit()
                    else:
                        print("\nInvalid input, please enter \"fight\".")
                        continue
            else:
                print("\nWrong answer, try again.")
                continue
            
    #monster path
    elif choice_boss == "monster":
        print("\nYou walk up to the door and you see that you have a riddle to solve.")
        time.sleep(2)
        riddle_answer_monster = ""
        
        while riddle_answer_monster != "1694":
            print("\nThe riddle is as follows:\n\nFind the four digit number in which the first digit is one fourth\n"
                  "of the last digit, the second digit is 6 times the first digit,\n"
                  "and the third digit is the second digit plus 3. What number is it?")
            riddle_answer_monster = input("> ")
            if riddle_answer_monster == "1694":
                print("\nCorrect!")
                time.sleep(2)
                print("\n\nThe door opens and you are in a big room full of treasure chests!\n"
                      "You see two red light in the dark corner of the room. A big armoured\n"
                      "beast emerges from the dark corner, ready to defend his treasure.")
                fight_monster = ""
                
                while fight_monster != "fight":
                    print("\nEnter \"fight\" to begin the fight.")
                    fight_monster = input("> ")
                    
                    if fight_monster == "fight":
                        if choice_weapon == "spear":
                            print("\nThe monster charges at you and brace yourself with your spear\n"
                                  "in front of you. The spear goes cleanly through the monster's armour.\n"
                                  "The monster is badly wounded by his charge. You put an end to his\n"
                                  "misery by piercing the spear right through his heart. You loot\n"
                                  "the room and leave. Fame and riches are now yours!\n\nYOU WIN")
                            sys.exit()
                        else:
                            print("\nYour great axe can't penetrate the monster's armour.\n"
                                  "You get completely mauled by the monster.\n\nGAME OVER")
                            sys.exit()
                    else:
                        print("\nInvalid input, please enter \"fight\".")
                        continue
            else:
                print("\nWrong answer! Hint: first digit is 1.")
                continue
    else:
        print("\nInvalid input, please enter \"necromancer\" or \"monster\".")
        continue
    
    
  
    
   
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 