# Nikolas S Fisher
# Date: 10/19/2022
#
# Description: Upon arriving at the SOS signal you find an abandoned space station.
# Once inside landing bay you notice a ship and 3 other areas to explore.
#
# Options:
#       1. Look at ship/take ship to planet
#       2. Explore quiet passage on right ( - health, - flashlight)
#       3. Explore noise from passage in front (+ military rifle, +1 med pouch, + Military grade Oxygen Tank
#           *For 3 you must need flashlight*
#       4. Explore control room in landing bay (+ info about ship and max ammo/1 med pouch)
#
import time

import main_character as mc
import ACT3_THE_DWELLING_CITY
import ACT1_SOS

def start():
    mc.init_glabal_vars()
    hangarstorage = 0
    hangarstorage1 = 0
    spaceattack = 0
    #chapter2_success = 0
    choice1a_chosen = 0
    # while chapter2_success == 0:
    print("Act 2: 'The Only Hope'\n\n\n\n")
    # input()
    time.sleep(2)

    print("Tyson's ship begins its approach towards the SOS signal. He notices\n"
          "a space station that seems to be damaged. Before docking Tyson circles\n"
          "the station and sees no sign of life. As Tyson heads towards the hanagar\n"
          "he notices a logo of an ancient research organization on the side of\n"
          "the station. As the ship is landing in the station, Tyson notices a unique\n"
          "looking ship in the hangar.\n\n\n")
    # input()
    time.sleep(5)

    print("Tyson:\n\n"
          "'I need to explore this ship, there might be some clues to what this is doing\n"
          "here.'\n\n"
          "As Tyson leaves the ship he hears a beeping noise coming from a corridor.\n"
          "Along with that there seems to be another hallway and a control room for the"
          "hangar.\n\n\n")
    time.sleep(4)

    print("Tyson:\n\n"
          "'I guess its too late to turn back. I'll just keep pressing forward. I'm\n"
          "soon close.'\n\n\n")

    while choice1a_chosen == 0:                     # Keeps user in a while loop until this variable is updated.
        choice1a = input("Please pick one of the 4 options:\n"
                             "1. Investigate unique looking ship\n"                         # Change this option to be number 3
                             "2. Explore the passage with noise on right\n"                  # So all correct choices are 1
                             "3. Explore the quiet passage\n"
                             "4. Check out the control room for hangar\n\n"
                             "Selection:\n\n\n")

        if choice1a == "1":
            if "KEYS" in mc.inventory:
                station_choice = 0
                while station_choice == 0:
                    print("Tyson has the keys to the ship and is able to leave the station\n")
                    station = input("Do you want to continue to explore the station or leave the station?\n"
                                    "1. Keep Exploring\n"
                                    "2. Leave Space Station\n")
                    if station == "1":
                        station_choice += 1
                    elif station == "2":
                        station_choice += 1
                        choice1a_chosen += 1
                        mc.inventory.remove("KEYS")
                        print(mc.inventory)
                        print("Tyson:\n\n"
                              "'Its time to put this thing to the test...'\n")
                        time.sleep(4)
                        ACT3_THE_DWELLING_CITY.start()
            else:
                print("You do not have the required item to enter the ship..\n"
                      "MISSING ITEM: KEYS\n")

            # print("Tyson tries getting into the ship and is unable to open it. It seems\n"
            #       "like a key is needed.")               # Option that allows Tyson to move forward next chapter
            #choice1a_chosen = 1
            #print("For the sake of testing we pick the lock and get in.")
            #ACT3_THE_DWELLING_CITY.start()

# Path 2 will lead the player to a fight. If the player wins the fight, they will go on to find the keys to the ship in
# a room, along with a Med Pouch
        elif choice1a == "2":
            # spaceattack = 0
            if spaceattack == 0:
                spaceattack += 1
                print("You open the blast doors to the passage way and notice it\n"
                      "is pitch black. You grab your flashlight from your bag and\n"
                      "attach it to your current weapon and begin moving through the\n"
                      "the darkness of the passage way. As you advance forward you hear\n"
                      "the noice coming from ahead begins sounding like a humans voice. Holding\n"
                      "out hope that there is a survivor on this station you rush forward.\n\n")

                time.sleep(6)

                print("As you rush towards the sound a someones voice you\n"
                      "fail to check your surroundings and before you can get\n"
                      "to the source of the sound, something jumps out of the\n"
                      "darkness and attacks knocking you to the ground. As you\n"
                      "get to your feet you see two other entities standing\n"
                      "behind the one that attacked you.\n")
                time.sleep(5)

                print("You need to stand and fight\n")
                # spacewal
                # while spacewalkerintro == 0:
                print("Entity: Space Walker\n"
                      "Health: 50 HP")
                print(
                    "The Space Walker seems to be a humanoid entity covered in a black metalic like substance. It body is\n"
                    "always twitching and convulsing. Mimicing the voice of any creature it orginally was.\n ")
                time.sleep(3)

                # spacewalkerintro += 1
                time.sleep(2)
                # This is the start of the combat, this is going to continue to loop until either the player or monsters
                # health reaches 0
                playerchoice = 0
                combat1 = 0
                while combat1 == 0:

                    while playerchoice <= 0:
                        attack_heal = input("Please pick a choice:\n"
                                            "1.Attack\n"
                                            "2. Heal\n")

                        if attack_heal == "1":
                            mc.sp.health = mc.attack(mc.sp.health)
                            time.sleep(2)
                            playerchoice += 1
                            print("Tyson's HP:", mc.tyson.healthpoints)
                            print("Space Walker's HP:", mc.sp.health)
                            print()
                            # if mc.sp.health <= 0:
                            #     break

                            # if mc.tyson.healthpoints or mc.sp.health <= 0:
                            #     combat1 += 1
                            #     #break
                            time.sleep(2)
                        elif attack_heal == "2":
                            mc.tyson.healthpoints = mc.healing(mc.tyson.healthpoints,mc.sp.health)
                            playerchoice += 1
                            print("Tyson's HP:", mc.tyson.healthpoints)
                            print("Space Walker's HP:", mc.sp.health)
                            print()
                            time.sleep(2)
                        else:
                            print("Please pick a valid option...")
                            time.sleep(2)

                    if mc.sp.health <= 0:
                        combat1 += 1

                    mc.tyson.healthpoints = mc.monster_attack(mc.tyson.healthpoints, mc.sp.entitynum)
                    # if mc.tyson.healthpoints or mc.sp.health <= 0:
                    #     combat1 += 1
                    #     # break

                    print("Tyson's HP:", mc.tyson.healthpoints)
                    print("Space Walker's HP:", mc.sp.health)
                    print()
                    time.sleep(2)
                    playerchoice -= 1


                        # if mc.tyson.healthpoints <= 0:
                        #     mc.combat1 += 1
                        #
                        # elif mc.tyson.healthpoints <= 0:
                        #     mc.combat1 += 1

                if mc.sp.health <= 0:

                    print("You defeated the Space Walker, and the other two ran away. As the run away Tyson shoots his pistol\n"
                          "at a expose circuit. This causes it to arc hitting both entities, burning them to a crisp.\n\n\n ")
                    time.sleep(2)

                    print("You keep walking through the hallways with your pistol and flashlight at the ready. After a little\n"
                          "searching you find no more Space Walkers and discover a research lab with the keys to the ship\n"
                          "in the hangar.\n\n")
                    time.sleep(1)
                    mc.inventory.append("KEYS")                     # Having this string in users inventory allows for them
                                                                    # to gain access to the new ship and leave to next ACT
                    print(mc.inventory)
                    time.sleep(2)
                    print("Before you go back you check the lab for any additional supplies and find a MED POUCH")
                    mc.inventory.append("MED POUCH[MP]")
                    print(mc.inventory)
                    time.sleep(2)
                    print("Tyson:\n"
                          "'I should head back to my ship, these keys might belong to that weird looking ship in\n"
                          "the hangar.")
                    combat1 += 1

                    # chapter2_success = 1
                    # ACT3_THE_DWELLING_CITY.start()

                elif mc.tyson.healthpoints <= 0:
                    combat1 += 1
                    print("You were defeated by the Space Walker...\n\n")
                    exit()

            else:
                print("You have explored this area...")

        elif choice1a == "3":

            if hangarstorage == 0:
                print("You explore the quiet corridor and end up at the control room for\n"
                      "for the space station. You also find more info about research group\n"
                      "and planets. As you continue clearing the room you find a corspe laying\n"
                      "over a control panel broadcasting the SOS signal. Next to the body lies a\n"
                      "MED POUCH, and a MILITARY RIFLE")
                mc.inventory.append("ATOM RIFLE[AR]")
                mc.inventory.append("MED POUCH[MP]")
                print("Tyson:\n"
                      "'Looks like we got some new gear!\n", "Inventory:", mc.inventory)
                time.sleep(2)
                hangarstorage += 1

                print("Tyson:\n"
                      "'I found the source of the signal, now I need to find out what happened\n"
                      "here. I should back to the hangar, maybe there is somewhere else we can go.")

            else:
                print("You have already visited this area and collected all the loot...")

        elif choice1a == "4":
            if hangarstorage1 == 0:
                print("You go into control room and find a document regarding the ship and what happened\n"
                      "here. Along with that you found: BANDAGE.")
                time.sleep(4)

                print("PROTOTYPE 0-3 Model 'GeoTerria':\n"
                      "The GeoTerria is a ship designed to withstand the extreme atmospheres and climates\n"
                      "of planets. This is done by using nano-technology to fully be able to adapt to any\n"
                      "environment. Our team was sent to this star system to find a hidden civilization with\n"
                      "the answer to the creation of a deadly disease named 'Solar Spores'. We haven't even\n"
                      " been able to set foot on any of the planets. This prototype is the third iteration\n"
                      "after two failed attempts. This might be out last chance. The disease we have been\n"
                      "studying seems to be evolving and if this progression stays consistent it might have\n"
                      "the ability to overtake all life on a whole planet or even a whole solar system.\n")
                mc.inventory.append("BANDAGE[B]")
                print(mc.inventory)
                time.sleep(6)

                print("Tyson:\n"
                      "'If this information is accurate our only bet to checking out these planets is that\n"
                      "ship in the hangar. God dam it, I'm putting my life in a prototype... great!\n\n'")
                time.sleep(3)
                print("Before you are about to leave you notice something a device locked in a clear container.\n"
                      "You break the lock and find a small hand held device with a paper document with a description.\n"
                      "The device is named the quantum adapter, and supposedly it ability to break down any piece\n"
                      "hardware, technology, and weaponary into a form of energy. This form of energy can be adapted\n"
                      "and constructed anywhere else integrating into new technologies and systems automatically.\n")
                time.sleep(8)
                print("After reading this, you decided that this device might come in handy in the future and take it..\n")
                mc.tools.append("ADAPTER")
                print()
                print("Tools:", mc.tools)
                mc.adapter += 1
                time.sleep(2)
                print("Tyson heads back to the hangar\n")
                time.sleep(2)
            else:
                print("You have already visited this area and collected all the loot...")
        else:
            print("Please pick a valid option.\n")                     # allow for options to be repeated

