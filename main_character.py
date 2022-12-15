# Nikolas S Fisher
#
# 11/2/2022
#
#
# This program will contain the variables for the main character Tyson Barrel when starting the game. It will contain
# oxygen, health, name, inventory, weapons, attack, tools.
#


import random

#import main_character
import time



# Global Variables


def init_glabal_vars():
# Global variables
    global tyson
    global Tyson
    global inventory
    global tools
    global health
    global monster_health
    #global tyson_oxgyen
    global weapons
    global sp


    #global healing_chosen
# Chapter 1 Choices
    global chapter1_success
    global choice1_chosen
    global cheater
    global cs_check

# Chapter 2 Choices
    global chapter2_success
    # global choice1a_chosen
    # global spacewalker_chosen
    global adapter
    #global combat1

# Chapter 3 Choices
    global chapter3_success

# Chapter 4 Choices
    global chapter4_success
    global plasmabeam

#Chapter 5 Choices
    global chapter5_success


    global space_walker

    global spacewalkerinto



# def hptracker(tysonhp, mhp, wdp, mdp, chance, monster):
#     print("You engaged in combat with " + monster)
#
#     battle_TEMPLATE.start(tysonhp, wdp, mdp, chance )

class tyson:
    healthpoints = 250
    oxygen = 300
    inventory = ['Flashlight', 'Pistol', 'Bandage', ]
# global Tyson #globalizes Tyson, letting you update and access his attributes more easily
Tyson = tyson #creates a tyson class object called Tyson
# print("Your HP is " ,Tyson.healthpoints) #prints the Tyson object's health
# Tyson.healthpoints -= 50 #updates Tyson's health to be 50 less than it started
# print("Your health is now", Tyson.healthpoints) #should be 50
#Tyson.healthpoints #how we would reference Tyson's HP in another module


class space_walker():
    health = 50
    attack = 10
    entitynum = 1
sp = space_walker


class giant():
    health = 250
    attack = 75
    entitynum = 3
Giant = giant

class glowguy():
    health = 500
    attack = 100
    entitynum = 4
glow = glowguy

class fist():
    attack = 5
    selfdamage = 2
    weaponnum = 1
class pistol():
    attack = 15
    weaponnum = 2

class hawkins_emitter():
    attack = 200
    weaponnum = 3

combat1 = 0
spacewalkerintro = 0
cs_check = 0

# This function is dedicated to the attack from the main character. It takes tyson and monster's health as parameters.


def attack(monster):

    #tyson = tyson.healthpoints
    #print("TESTTTT")
    # tysonb = tyson.healthpoints
    # monster = sp.health
    #tyson.healthpoints = tysonb
    # attack_chosen = 0
    # while attack_chosen == 0:               # This allows the user to keep trying to insert a valid option until a valid choice is inserted.
    #     attack_choice = input("Please pick a course of action:\n"
    #                           "1.Attack\n"
    #                           "2. Heal\n")
    #
    #     if attack_choice == "1":            # This If Else statement is for whether the player wants to attack or heal,
    #                                         # this statement is if the player chooses to attack the enemy
    #         print("You have chosen to attack.")
    #         time.sleep(1)
    #         attack_chosen += 1

    weapon_chosen = 0

    while weapon_chosen == 0:           # While loop to allow player to pick a weapon from inventory
        print(inventory)
        weapon_choice = input("Please pick a weapon from your inventory:")
        #weapon_choice.upper()
        #if weapon_choice in inventory:
        # weapon_chosen = 1
        if weapon_choice == "F":
            weapon_chosen += 1
            if tyson.healthpoints > 0:
                print("Tyson decides he wants to use a Flashlight to fight... ")
                print("You were somehow able to hit the enemy once.")
                # tyson.healthpoints -= 2
                monster -= 5
                print("Tyson's Health:", tyson.healthpoints)
                print("Monsters Health:", monster)
                print()
                time.sleep(4)

            # elif tyson.healthpoints <= 0:
            #     print("Tyson's body has taken too much damage and can't keep going\n")

        elif weapon_choice == "P":          # If the player decides to use a PISTOL to attack
            weapon_chosen += 1
            print("Tyson draws his pistol aiming down the barrel at the monster, firing\n"
                  "off one shot hitting the monster.\n ")
            combop = random.randrange(1, 2)
            if combop == 1:
                monster -= pistol.attack                      # The gun does 15 damage to the enemy, taking away 15 HP
                return monster

            elif combop == 2:
                combo = pistol.attack * 2
                monster -= combo
                print("You were able to accurately hit the enemy three times\n")
                return monster
            if monster <= 0:
                return monster
                #print("You have killed the monster with your pistol\n")
                #combat1 += 1
            time.sleep(2)

            print("Tyson's Health:", tyson.healthpoints)
            print("Monsters Health:", monster)
            time.sleep(2)

            #return tysonb and monster
            # return space_walker and health
        elif weapon_choice == "AR":
            weapon_chosen += 1
            print("You have chosen to use the ATOM RIFLE")

            combo1 = random.randrange(1,4)

            if combo1 <= 2:
                print("You have hit the enemy with a shot from the rifle")

                monster -= 30
                return monster

            else:
                print("Your focus is on point and you hit 3 consecutive shots on the enemy.\n")
                monster -= 90
                return monster

        elif weapon_choice == "HE":
            weapon_chosen += 1
            print("You have chosen to use the Hawkins Emitter")

            blackhole = random.randrange(1,5)

            if blackhole == 6:
                print("You throw the device and its opens exposing a black hole.... it starts to suck in\n"
                      "everything around it!")
                print("As it takes down your enemy, it keeps going with no end in sight... The black hole\n"
                      "starts getting bigger as it consumes more matter, before you know it the containment\n"
                      "device is gone too....\n\n")
                time.sleep(2)
                print("The black hole is getting out of hand... you try running away but it is too strong\n"
                      "and pulls you in.... ")
                print("You have died from your own attack....\n")
                time.sleep(5)
                print("Thank you for playing!")
                exit()
            else:
                print("You throw the device near the enemy and it opens revealing a black hole on the inside.\n"
                      "The black hole starts sucking matter from the monster, dealing a lot of damage..\n\n"
                      "After a few seconds the device closes...\n")

                monster -= 200
                return monster

        # Weapon Choice equals Cosmic Judgement
        elif weapon_choice == "CJ":
            weapon_chosen += 1
            print("Tyson:\n"
                  "'I was hoping I wasn't going to have to use this'\n\n"
                  "You begin focusing on your enemy and a power within you starts to reveal itself\n"
                  "Your eyes begin to flow a bright purple, and your body starts emitting lighting.\n"
                  "You begin to rise in the air and raise your arm to point at the being in from of\n"
                  "you. A large beam of lighting engulfs it.\n")
            monster -= 500
            print("Tyson's Health:", tyson.healthpoints)
            print("Monsters Health:", monster)
            return monster
        else:
            print("Please pick a valid input.")

# This portion of the code will be dedicated for healing, if that is the path that is chosen.
def healing (tysonb, monster):

            #attack_chosen += 1               # Stops the while loop asking for the players attack/heal question
    healing_chosen = 0
    while healing_chosen == 0:          # A while loop that keeps asking for player to pick a valid heal from
                                        # their inventory
        print(inventory)
        healing_choice = str(input("Please selecting a heal from your inventory:\n"))
        #if healing_choice in inventory:
        # healing_chosen += 1
        if healing_choice == "B":
            print("You decide you need to heal the injuries you have taken instead of attacking\n")
            tysonb += 25
            print("Tyson's Health:", tysonb)
            print("Monsters Health:", monster)
            print()
            inventory.remove("BANDAGE[B]")
            time.sleep(3)
            healing_chosen += 1
            return tysonb


        elif healing_choice.upper() == "MP":
            print("You decided you have taken too much damage and really need heals instead of attacking.\n")
            tysonb += 50
            # Need to add a limit to health
            print("Tyson's Health:", tysonb)
            print("Monsters Health:", monster)
            print()
            inventory.remove("MED POUCH[MP]")
            time.sleep(3)
            healing_chosen += 1
            return tysonb
        else:
            print("Please select a valid choice.\n")
            time.sleep(2)


            if "Bandage" and "Med Pouch" not in inventory:
                print("You do not have any heals and have missed your turn...\n")
                time.sleep(3)
                break

            # healcount = 0
            # while healcount == 0:
            #     heal = input("You might not have anymore heals...\n"
            #                  "Would you like to try healing again?\n"
            #                  "1.Yes\n"
            #                  "2.No")
            #     if heal == "1":
            #         healcount += 1
            #
            #     elif heal == "2":
            #         break



    # else:
    #     print("Please select one of the options.\n")

#print("Tyson attacks with", weapon_choice )

# This function is part of the combat of the game. This deals with the monsters attack. Taking the player's health, and
# the monsters entitynum. This variable is used identify what monster is fighting
def monster_attack(tysonb, monster):

    if monster == 1:
        # spacewalkerintro = 0
        # while spacewalkerintro == 0:
        #
        #     print("Entity: Space Walker\n"
        #           "Health: 50 HP")
        #     print("The Space Walker seems to be a humanoid entity covered in a black metalic like substance. It body is\n"
        #           "always twitching and convulsing. Mimicing the voice of any creature it orginally was. ")
        #     time.sleep(3)
        #     input()
        #     spacewalkerintro += 1

        print("The Space Walker comes charging at you at an alarming speed. Before you can even react it is right in front\n"
              "you swinging its sharps claws at you.\n")
        time.sleep(1)
        dodge = random.randrange(1, 3)
        if dodge < 3:           # If dodge is less than 3 (1,2) player will take damage.
            print("Tyson was unable to dodge and got caught up in the claws of the Space Walker's attack.\n")
            tysonb -= 25
            print("Tyson's HP:", tysonb)
            time.sleep(4)


            if tysonb <= 0:
                print("You have taken too much damage and the Space walker gains the upper hand. It takes the opportunity\n"
                      "to deal the final blow to you, killing you on the spot and assembling you as another space\n"
                      "walker\n")
                #combat1 += 1

                return tysonb
            return tysonb

        elif dodge == 3:
            print("Tyson was able to dodge the attacks from the enemy.\n ")
            time.sleep(3)
            return tysonb

    elif monster == 2:
        print()

    elif monster == 3:
        print("Entity: Unknown......\n"
              "Description: Giant Humanoid creature towering into the clouds...\n")
        time.sleep(1)

        dodge = random.randrange(1,4)

        if dodge < 4:
            print("By some miracle you dodge the literal mountain of debris and only ended up with a few bruises\n"
                  "and scratches. -20 HP")

            tysonb -= 20
            print("Tyson's Health: ", tysonb)

            if tysonb <= 0:
                print("Even dodging wasn't enough to keep you away from death's doorstep. You were killed by the\n"
                      "unknown entity.")

                return tysonb

            return tysonb
        elif dodge == 4:
            print("The force from the kick has knocked you off your feet. As you look up the mountain of debris\n"
                  "is hurling towards you. With no time to react, a large piece of the mountain hits you directly.\n"
                  "The impact causes you to be flung with the debris causing signifcant damage. -75 HP")

            tysonb -= 75

            print("Tyson's health:", tysonb)
            print()
            time.sleep(4)

            if tysonb <= 0:
                print("No matter how tough you thought you were, you don't stand a chance against something that\n"
                      "can casually kick mountains miles....")
                return tysonb

            return tysonb
# This elif statement is if monster equals 4. This means the monster attacking is the glowing entity from the last act
    elif monster == 4:
        dodge = random.randrange(1,4)

        if dodge == 4:
            print("The entity starts charging up his attack. While it is doing this, it starts glowing brighter and\n"
                  "brighter before you can't look anymore. \n")
            print("You activate your ability too at the last moment. Dodging the incoming light beam...\n")
            return tysonb

        else:
            print("The entity starts glowing and before you can even react a beam of light hits you directly\n"
                  "dealing a significant amount of damage. -100 HP")
            tysonb -= 100

            if tysonb <= 0:
                print("That attack was too much for Tyson to handle....")
                return tysonb

            return tysonb

# def globalvariables():
#     global playername
#     global weapon_list





    tyson = "Tyson Barrel"

inventory = ["FLASHLIGHT[F]", "PISTOL[P]", "BANDAGE[B]"]
tools =[]
adapter = 0
plasmabeam = 0


oxygen = 300
weapons = ["FIST", "PISTOL", "RIFLE", "FLASHLIGHT", "COSMIC JUDGEMENT"]
#health = 250


#combat1 = 0
# Weapons


# Oxygen Tanks

standard_O2 = 200       # This will contain the duration the player has oxygen.
milgrade_O2 = 350       # Affected by decisions made in game.
O2_recycler = 500






    #def comabat(player_turn,enemy_turn):

# Monsters Health
#space_walker = 50


# Chapter Trackers

# # Chapter 1 Choices
# chapter1_success = 0
# choice1_chosen = 0
# choice1a_chosen = 0
cheater = 0

# # Chapter 2 Choices
# chapter2_success = 0
# spacewalker_chosen = 0
#
# # Chapter 3 Choices
# chapter3_success = 0
#
# # Chapter 4 Choices
# chapter4_success = 0
#
# # Chapter 5 Choices
# chapter5_success = 0
#
