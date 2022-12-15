# Nikolas S Fisher
# Date: 10/19/2022
#
# Description: Tyson final is able to get past storm and goes into a massive cave. Tyson scans the cave and finds 4
# areas of interest.
#
#
# Options:
#       1. Explore Ancient Structures(Allows you to progress into next chapter)
#       2. Explore crash site (Find legendary oxygen tank and info about this prototype ship)
#       3. Explore glow (Get attacked and loose health and oxygen)
#       4. Keep descending (Die)
import random
import time

#
#
#

import main_character as mc
import ACT4_THE_TEMPLE_OF_THE_GODS


def start():
    act3_success = 0

    # ACT 3 INTRODUCTION: This section will give a brief explanation of the entry of the planet and setting up for the
    # players decision
    print("Act 3: The Dwelling City")
    # input()
    time.sleep(3)

    print("Upon arriving at OMEGA-ZED-864 you cross your fingers in hope this new ship is able to adapt to the harsh\n"
          "climate of this planet. As you descend into the atmosphere acidic rain begins pouring all around the ship\n"
          "and any effort to avoid it without leaving the atmosphere seem fruitless. As the ships systems begin detecting\n"
          "breaches from acidic rain, the automated nano system takes over and adapts and covers the exterior of the\n"
          "ship in a hard shell.\n\n")
    time.sleep(2)
    print("As you almost tear up with joy from the prototype ship working, you have the scanners focus on mapping out\n"
          "terrian below, giving you a better understanding of where to look for the eight information.")
    print("After a few minutes of flying you come across a large hole in the planet leading down to a large cave\n"
          "system. With it being the only thing you have noticed in miles you take a chance exploring it. As you\n"
          "begin descending you notice multiple path ways show up on the scans of the cave network. With that you\n"
          "also notice a crash site from what seems like a previous exploration. After a minute of a more through\n"
          "scan, it also identifies some structures. There is also something weird on the scan... a big flash red\n"
          "'X' over the hole going deeper. I have never seen that before....\n\n")

    weaponcheck = 0         # This will check to see if the player has already picked up the loot from the crash site

    plasmacheck = 0         # This will check if player picked up plasma canon.

    depthcheck = 0          # Checks if the player has gone deeper in cave, prevents from going down again.

    choice_chosen = 0       # This will allow for the player to continue to make choices as long as this is not updated.
                            # Along with that is will check for user input so if it is invalid they can keep trying.
    while choice_chosen == 0:
        choice1b = input("Options:\n"
                         "1. Investigate the crash site\n"
                         "2. Explore the ancient structures that showed up on scanners\n"
                         "3. Get closer to glow to examine further\n"
                         "4. Keep descending deeper into the cave\n"
                         "5. Leave planet\n"
                         "Selection:")

# Choice 1: This will have the player check out a crash site that showed up on the ships scanners. During this selection
# the player will get two new items automatically(HAWKINS EMITTER, MED POUCH). BUt if they acquired the ADAPTER they
# can get a plasma beam and add it to their own ship.
        if choice1b == "1":
            print()
            print()
            print("You go to crash site and find new info about company.\n"
                  "And you find a new item called a Hawkins Emitter, and med pouch.\n\n"
                  "You examine the documents closer and discover that this ship was the first prototype named GeoDigger\n"
                  "This ship had the same capabilites as this model but with the addition of digging massive tunnels in\n"
                  "the planet. The system log mentions how the entrance was artificial, these cave systems were already\n"
                  "here and there is something lurking in the shadows. ")
            print("The tool used to dig this entrance is said to be a massive plasma beam cannon that mounts on the\n"
                  "front of the ship and consumes so much power it can only be used once every two days. Firing it\n"
                  "more than its limit will drain all possible energy from your ship, leaving you stranded where ever\n"
                  "you are....")
            time.sleep(3)
            print("The last log mentions something about a glow... and then cuts off.")
            time.sleep(1)

# This IF statement checks to see if the player grabbed the ADAPTER tool. If so it will update variable plasmabeam
# which can be used in ext chapter.
            #if "ADAPTER" in mc.tools:
            # if plasmacheck == 0:
            if mc.adapter >= 1:                     # If adapter has been updated this new branch becomes possible.
                if plasmacheck == 0:                # Player has the ability to get a new addition to their ship
                                                    # Opens new branch in next chapter.
                    print("Tyson:\n\n"
                          "'Wait I might be able to use that ADAPTER tool to take this digging technology...it could be\n"
                          "used for offensive purposes.'")
                    print("Tyson uses the adapter and adds this new tech to his ship.")
                    time.sleep(2)
                    mc.plasmabeam += 1          # This updates the variable and will allow for this tech to be used in the
                                                # next ACT.
                    plasmacheck += 1
                else:
                    print("You have already grabbed all any useful technology.")
# This section will happen no matter is the player has the ADAPTER, giving them A HAWKINS EMITTER and MED POUCH.
            if weaponcheck == 0:                                # This will check to see if player has already grabbed
                                                                # loot at the crash site.
                mc.inventory.append("HAWKINS EMITTER[HE]")
                mc.inventory.append("MED POUCH[MP]")
                print("Tyson's Inventory:", mc.inventory)
                print("I have no idea what this HAWKINS EMITTER is seems like I am able to throw it....\n"
                      "It kinda reminds me of some scientist from this back water planet in the Milky Way galaxy,\n"
                      "I think his name was like Steven Hawkins or something like that... huh small universe'")
                time.sleep(4)
                weaponcheck += 1                    # Updates variable to show that player has already gotten loot

            elif weaponcheck >= 1:                  # Is used if the player has already looted the crash site
                print("You have already collected the loot from this crash site...")
                time.sleep(2)



            # You acquire med pouch, new oxygen tank, and new plasma weapons and med pouch)
            # Nested if- else statements for exploring crash-site, finding ship log, gear, etc..

# This IF statement is if the player decides to go towards the ancient structures on the scanners.
        elif choice1b == "2":
            print("You decide the best course of action is to get to head towards the ancient structures.. \n\n")
            time.sleep(2)
            print("Tyson lands the ship just outside what seems to be a ancient underground city.\n"
                  "You exit the ship move towards some of the structures. You go from structure to structure, only\n"
                  "finding ruins.\n"
                  "However, as you move towards what seems to be the center of the 'city' you notice one building\n"
                  "that seems to be untouched by any sort of disaster.\n\n ")
            time.sleep(7)

            print("You heads toward the structure with you guard up, ready for anything... \n"
                  "Right as you are about to get a few feet away from it a door opens in front of you.\n"
                  "You hesitate before making your way inside.\n\n")
            time.sleep(5)

            print("Upon entering you realize this is some kind of place of worship, with a isle straight down the\n"
                  "middle. At the other end a shadowed entity standing behind a podium.....\n"
                  "As you lift your foot to take a step forward the entity speaks.\n\n")
            time.sleep(3)
            print("Shadow Entity:\n\n"
                  "'This is not the place you seek... for there is clearing on a the farthest planet from this place.\n"
                  "But getting to this clearing will be no easy feat, as it rains purple lightning and is guarded always.\n"
                  "Hed my warning traveler, no matter how strong the powers sleeping inside you is you can't beat the\n"
                  "Titan...\n\n")
            time.sleep(6)
            print("But if you do make your way down to the clearing you will find a temple, in that temple there is a\n"
                  "hidden scriptor underneath the the podium in the center of the structure. It is said that in this\n"
                  "scriptor that it holds the location to some sort of bridge or gateway to somewhere behind our\n"
                  "reach.\n")
            time.sleep(6)
            print("Before you can respond to the entity it vanishes...\n"
                  "You decide this is not any place to be hanging out and decide to head back to the ship.\n\n")
            time.sleep(6)

            act3_success += 1               # This will allow the player to leave the planet and rather than orbit
                                            # planet it goes to next ACT

            #choice_chosen += 1


            # Add nested if-else statements for the opportunity to explore different structures/ talk to NPC to
            # gather information on where necessary information regarding the next location. Looking for temple

            # To get to this point need to find chapel in nested If-Else statement
            #ACT4_THE_TEMPLE_OF_THE_GODS.start()
# This IF statement will have the player head towards a glow down one of the tunnels.
        elif choice1b == "3":
            print("You begin heading down the tunnel that has the glow coming from it..")
            print("As you get closer you notice there is something lurking in the darkness behind the blow.\n"
                  "After a second glance you realize that light is part of whatever creature lurking in the\n"
                  "darkness.\n")
            time.sleep(4)
            glow = random.randrange(1, 2)               # This variable will either be a 1 or 2 causing two different
                                                        # outcomes

            if glow == 1:           # The player escapes an attempted attack
                print("Your instincts kick in and you grab the controls and steer the ship away...\n"
                      "Right as you begin heading away from it, the creature lungs out toward the ship..\n")
                time.sleep(2)
                print("Out of luck you were able to get away from its clutches...\n"
                      "When your far enough away you turn around to see if it is chasing you and notice it has\n"
                      "done back to its original positioning looking like some mysterious glow.\n\n")
                time.sleep(3)

            else:                   # The player gets caught up in an attack by a monster
                print("Your instincts kick in and you grab the controls and steer the ship away...\n"
                      "Right as you begin heading away from it, the creature lungs out toward the ship..\n")
                time.sleep(2)
                print("You weren't fast enough and the creature grabs the ship with its mouth.\n"
                      "It tries biting down on the ship but the automated adaption system keeps it from doing\n"
                      "any serious damage and it throws the ship a back causing it to hit the wall of the cave.\n\n")
                time.sleep(3)
                print("This throw by the creature has caused Tyson to hit his head against the ships control panels.\n"
                      "-10 Health points\n")
                mc.tyson.healthpoints -= 10                 # Damage is caused to the player, - 10 HP
                print("Tyson's Health:", mc.tyson.healthpoints)
                time.sleep(4)

            # Give player opportunity to pick course of action, either engage ships weapons system or emergency evacuation
            # protocol (If weapons system, 50% chance to kill monster 50% chance of getting causing serious damage to ship
            # and player. If emergency protocol, 80% chance to escaping and 20% chance of taking minor damages.(Will cause
            # player to lose a certain amount of oxygen depending on choice)
        elif choice1b == "4":
            if depthcheck == 0:                     # This checks to see if the player has already come down here before
                print("You keep going deeper, and you get to a point where the lights are not working.\n"
                      "Out of nowhere a huge monster comes out and swallows the ship whole\n\n")
                depthcheck += 1                         # This variable makes it, so you may only come down here once
                                                        # you learn from your mistake.

                depths = random.randrange(1, 5)          # creates a random variable within range 1, 5.
                                                        # It determines whehter you make it out.

                if depths < 4:                          # IF the number is less than 4, so (1, 2, 3) it will mean
                                                        # Tyson dies.
                    print("Tyson begins engaging all the fail safes to get out of this situation but nothing seems to be\n"
                          "working. The automated adaptive system is not able to fight against the natural acid created by\n"
                          "this monster. The ship rapidly breaks down leaving no trace.\n")
                    time.sleep(3)
                    print("Not too long after Tyson meets the same fate... ending the story of Tyson Barrel.\n")
                    print("By some miracle you are given another chance.\n")
                    depthcheck -= 1
                    deathchosen = 0
                    while deathchosen == 0:
                        deathchoice = input("You have fallen victim to the to hostile nature of the universe..\n"
                                            "You are either able to start over from the beginning of the ACT or exit.\n"
                                            "1. Restart chapter\n"
                                            "2. Exit Game\n"
                                            "Selection:\n")
                        if deathchoice == "1":

                            start()


                        elif deathchoice == "2":

                            exit()

                        else:
                            print("Please pick a valid option:\n")
                            time.sleep(2)

                else:                                   # Depths == 4 or 5 and this means that Tyson lives.
                    print("Tyson begins engaging all the fail safes to get out of this situation but nothing seems to be\n"
                          "working. When you think all hope is lost the ship's weapons start having an effect on the\n"
                          "monster.")
                    time.sleep(3)
                    print("The monster's mouth opens for brief moment and you see the light from the caves opening...\n"
                          "You max out the thrusters, jetting the ship upwards out of the monsters mouth.")

            else:                   # If depthcheck is updated to at least 1 ,character can not go down deeper again.
                print("Tyson:\n\n"
                      "'There ain't no way in hell am I going down there again that's crazy!")

# This option allows for the player to leave the planet. It will check whether the player has visited the ancient
# structures. If so they will have the ability to go to the farthest planet progressing the story to the next act.
# However, if they did not visit the structures they will orbit the planet taking time ot think
        elif choice1b == "5":
            if act3_success >= 1:
                print("You got what you needed from this place, its time to explore the farthest planet in the solar\n"
                      "system, OMEGA-ZED-866....")
                ACT4_THE_TEMPLE_OF_THE_GODS.start()
            else:
                print("You decided you need to take a step back to analyze the situation...\n"
                      "You got into orbit and think....")
                time.sleep(3)
                print("....")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("After multiple orbits of the planet you decide to return to the cave.\n\n")
                time.sleep(2)

        else:
            print("Please pick a valid choice:\n")
            time.sleep(1)
            #exit()          # allow for way to repeat the options
