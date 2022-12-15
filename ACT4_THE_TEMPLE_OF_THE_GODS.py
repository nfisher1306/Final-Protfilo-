# Nikolas S Fisher
# Date: 10/19/2022
#
# Description: Tyson descends into the final planet and gets past the insane storm and finds an
# area of land that is untouched by the storm and has clear skies. In that area there is a temple.
# Tyson lands in that area and sees a large creature approaching him.
#
# Options:
#       1. Run into the temple (allows you to get to next chapter)
#       2. Get into the ship and fly away (waits a day in orbit and tries again. -75 oxygen)
#       3. Stand and fight (looses all ammo and ends up looking dumb)
#       4. Charge creature  ( runs into storm and dies by lighting)
#
#
import time

import main_character as mc
import ACT5_BRIDGE_TO_EVERYTHING


def start():
    print("Act 4: 'The Temple Of The Gods'\n\n")
    time.sleep(3)

    print("Tyson arrives at the planet and begins descending, he is met with\n"
          "a fierce storm of purple lighting blanketing the sky with black fog\n"
          "as keeping visibility to a minimum. As the ship begins to take massive\n"
          "damage from the lighting, the automative systems on the ship begins\n"
          "adapting the ship to the current conditions of the planet.\n\n")
    time.sleep(5)

    print("After adapting to the environment Tyson heads for the marked location\n"
          "on the map. As he approaches the location there seems to be a temple at\n"
          "the marked location. If this planet wasn't already strange enough there\n"
          "is an absolutley no storm above it, just clear skies all the way up.\n"
          "Upon landing, Tyson gets out of the ship and the ground begins to shake.\n"
          "He turns around and there is a humanoid figure approaching. It is so tall\n"
          "that only the legs are visible up until the storm in the clouds. Before he\n"
          "can react the creature starts advancing toward him.\n\n")
    time.sleep(5)

    act4 = 0                # This variable is to check whether the player a valid choice to exit while loop
    act4o2 = 0
    while act4 == 0:            # allows player to keep trying to input a valid choice.
        choice1 = input("Tyson:\n\n"
                        "'Why does this shit always happen to me? Dam I can only think\n"
                        "of a few things, and I don't know if any of them will work...'\n\n"
                        "Options:\n"
                        "1. Run into the temple\n"                  
                        "2. Get into the ship and fly away\n"              # Can only pick this option 3 times before it is not longer a option
                        "3. Stand and fight\n"
                        "4. Charge creature\n"
                        "Selection:\n")

# This will have the player run into the temple if they choose 1. This is the right choice by it will allow you to find
# the information you needed.
        if choice1 == "1":
            print("You decide the best course of action is to hide from the 'Titan' in the temple.")
            print("After running into the structure you peak out looking at the activity of th beast and see it has\n"
                  "stopped moving closer.. After a brief pause the beast turns around and begins heading the other\n"
                  "way.")
            time.sleep(3)
            print("Once the 'Titan' is out of sight you begin searching the temple for the podium...\n"
                  "You find it after a brief search and begin to look for the hidden scriptor.")
            time.sleep(2)

            print("You find the scriptor you were told about from the mysterious shadow entity on the last planet.\n"
                  "After examining the scriptor you realize find the coordinators to somewhere else, talking about\n"
                  "a forbidden bridge to another realm...")
            print("You head back to the ship to enter these coordinators.")
            if mc.cheater >= 1:                 # If the player went to a different solar system in ACT 1 it will have
                                                # a different outcome.
                print("My scanner log says I scanned an unknown mass at these coordinators before, it must be at\n"
                      "that one star system I traveled to before. Wow how ironic I was so close...")
                time.sleep(2)
                print("Well lets head out and finally figure out what this bridge is really about..")
                ACT5_BRIDGE_TO_EVERYTHING.start()
            else:                               # If the player did not visit a new star system
                print("After entering them in, you depart this planet to discover what this so called 'bridge'\n"
                      "is really about...\n"
                      "Deep down you feel a sense of familiarity about this 'bridge' ")
                time.sleep(3)
                act4 += 1
                ACT5_BRIDGE_TO_EVERYTHING.start()
            input()
            # act4 += 1
            # ACT5_BRIDGE_TO_EVERYTHING.start()

# Will have the player orbit around the planet hopefully waiting

        elif choice1 == "2":
            # act4o2 = 0
            # while act4o2 < 6:
            if act4o2 < 5:
                print("You decide to wait for the giant to pass, but if you keep doing this, your ship won't be able\n"
                      "to keep up with the constant energy demand....")
                print("Once you make it to the clearing you see nothing has changed...")
                time.sleep(3)
                act4o2 += 1
                # act4o2 += 1

            elif act4o2 == 5:
                print("You have waited too many times... if you chose this option 1 more time, the ship's energy\n"
                      "supply will run out.\n\n ")

            elif act4o2 >= 6:
                print("You have tried to waiting too many times and the ship no longer has enough time to recharge\n"
                      "its systems, causing the life support systems to fail.......\n\n")
                time.sleep(2)
                print("This means the end of Tyson Barrel.\n")

                deathchosen = False
                while deathchosen == False:
                    deathchoice = input("You have died....\n"
                                        "Please pick your route:\n"
                                        "1. Restart current ACT\n"
                                        "2. Exit game\n"
                                        "Selection:\n")
                    if deathchoice == "1":
                        start()

                    elif deathchoice == "2":
                        print("Thank you for playing...")
                        time.sleep(2)
                        exit()

# You make a reckless choice and fight the giant
        elif choice1 == "3":
            print("You dont care about the odds you want to take your chances....")
            act4giant = 0
            AHchoice = 0
            while act4giant == 0:

                while AHchoice == 0:
                    attack_heal = input("Please pick a choice:\n"
                                        "1.Attack\n"
                                        "2. Heal")
                    if attack_heal == "1":
                        mc.giant.health = mc.attack(mc.giant.health)
                        time.sleep(2)
                        AHchoice += 1
                        print("Tyson's HP:", mc.tyson.healthpoints)
                        print("Space Walker's HP:", mc.giant.health)
                        print()
                        # if mc.tyson.healthpoints or mc..health <= 0:
                        #     act4giant += 1
                        #     break
                        time.sleep(3)

                    elif attack_heal == "2":
                        mc.tyson.healthpoints = mc.healing(mc.tyson.healthpoints, mc.giant.health)
                        AHchoice += 1
                        print("Tyson's HP:", mc.tyson.healthpoints)
                        print("Giant's HP:", mc.giant.health)
                        print()
                        time.sleep(2)
                    else:
                        print("Please pick a valid option...")
                        time.sleep(2)

                if mc.giant.health <= 0:
                    act4giant += 1

                mc.tyson.healthpoints = mc.monster_attack(mc.tyson.healthpoints, mc.giant.entitynum)

                # if mc.tyson.healthpoints <= 0:
                #
                #     act4giant += 1

                print("Tyson's HP:", mc.tyson.healthpoints)
                print("Space Walker's HP:", mc.giant.health)
                time.sleep(3)
                AHchoice -= 1

                # if mc.tyson.healthpoints <= 0:
                #     mc.combat1 += 1
                #
                # elif mc.giant.health <= 0:
                #     mc.combat1 += 1



            # mc.attack(mc.tyson.healthpoints, mc.giant.health)
            #
            # mc.monster_attack(mc.tyson.healthpoints, mc.giant.attack)


# If tyson's hitpoints drop to 0 or below it will update the while statement exiting the battle.
            if mc.tyson.healthpoints <= 0:
                print("Tyson was crushed by a mountain...")
                time.sleep(3)
                print("Thank you for playing... there is no getting up from a mountain crushing\n"
                      "you")
                act4giant += 1
                exit()
# If the giants hitppints drop to 0 or below it iwll update the while statement exiting the battle. This will also
# lead the player into the temple to find what he needs. This will lead to ACT 5
            elif mc.giant.health <= 0:
                print("Through sheer luck and plot armor you beat the giant!")
                time.sleep(1)

                print("After battling the behemoth you head into the temple. The second you reach the interior you\n"
                      "head to the podium in the center of the structure looking for the hidden scriptor.")
                time.sleep(2)
                print(
                    "You find the scriptor you were told about from the mysterious shadow entity on the last planet.\n"
                    "After examining the scriptor you realize find the coordinators to somewhere else, talking about\n"
                    "a forbidden bridge to another realm...")
                print("You head back to the ship to enter these coordinators.")
                act4giant += 1

            # If the player has visited the different star system in ACT 1. this outcome will pop up
                if mc.cheater >= 1:
                    print(
                        "My scanner log says I scanned an unknown mass at these coordinators before, it must be at\n"
                        "that one star system I traveled to before. Wow how ironic I was so close...")
                    time.sleep(2)
                    print("Well lets head out and finally figure out what this bridge is really about..")
                    ACT5_BRIDGE_TO_EVERYTHING.start()

            # If the player did not choose to visit the new star system, this outcome will happen.
                else:
                    print("After entering them in, you depart this planet to discover what this so called 'bridge'\n"
                        "is really about...\n"
                        "Deep down you feel a sense of familiarity about this 'bridge' ")
                    time.sleep(3)
                    ACT5_BRIDGE_TO_EVERYTHING.start()


# You make the most reckless choice ever and just charge the beast. The outcome will vary depending on previous choices
# made.
        elif choice1 == "4":
            # If the player was able to obtain the plasma beam they can shoot the monster with it rather than running
            # into the lighting storm. This will lead the player into the temple, then into the next ACT.
            act4 += 1
            if mc.plasmabeam >= 1:
                print("As you begin to think winning is impossible you remember that plasma canon you added to your\n"
                      "ship.")
                time.sleep(2)
                print("You run into the ship, start it up and aim for the right leg of this entity...The canon begins\n"
                      "charging and when it reaches fully power it releases a massive burst of energy drilling a\n"
                      "massive hole through the its right leg...")
                time.sleep(2)
                print("Seconds after a roar uncomparable to anything heard before echos across the entire planet\n"
                      "causing Tyson to drop to his knees in pain while trying to cover his ears through his suit.")
                time.sleep(1)
                print("You pass out form the noise and walk up hours later with no giant in sight.")
                print("After gaining your bearings you realize there is no threat in the area and you make your way\n"
                      "towards the structure in the middle of this abnormal clearing.")
                time.sleep(3)
                print("You find the scriptor you were told about from the mysterious shadow entity on the last planet.\n"
                      "After examining the scriptor you realize find the coordinators to somewhere else, talking about\n"
                      "a forbidden bridge to another realm...")
                print("You head back to the ship to enter these coordinators.")

                # If the player went to different star system in ACT 1, this outcome will play out.
                if mc.cheater >= 1:
                    print("My scanner log says I scanned an unknown mass at these coordinators before, it must be at\n"
                          "that one star system I traveled to before. Wow how ironic I was so close...")
                    time.sleep(2)
                    print("Well lets head out and finally figure out what this bridge is really about..")
                    ACT5_BRIDGE_TO_EVERYTHING.start()

                # If the player did not go to the new system in ACT 1
                else:
                    print("After entering them in, you depart this planet to discover what this so called 'bridge'\n"
                          "is really about...\n"
                          "Deep down you feel a sense of familiarity about this 'bridge' ")
                    time.sleep(3)
                    ACT5_BRIDGE_TO_EVERYTHING.start()

            # The player decided to charge the giant without thought, they did not have the plasma canon to use.
            # Resulting in their death.
            else:
                print("You run out towards in the monster, running into the storm\n"
                      "Tyson gets struck by lighting multiples times and dies.")
                exit()

        else:
            print("Please enter a valid choice....")
            time.sleep(1)

