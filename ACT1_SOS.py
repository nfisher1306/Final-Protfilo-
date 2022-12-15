# Nikolas S Fisher
# Date: 10/19/2022
#
# Description:This will be about Tyson's arrival at this uncharted solar system. Has 4 options. Respond to SOS signal,
# pick either of the two planets, or continue to explore space and leave.
#
# Options:
#       1.SOS signal(must do to progress) (Win)
#       2. Closest Planet(-oxygen)
#       3. Farthest Planet(-health/oxygen)
#       4. Keep exploring space (DIE)
#

import main_character as mc
import ACT2_THE_ONLY_HOPE
import ACT5_BRIDGE_TO_EVERYTHING
import random
import time


def start():
    mc.init_glabal_vars()

    print("Act 1: 'SOS'\n\n")

    print("Tyson's ship exited hyperspace and arrives at their destination,\n"
          "the uncharted solar system. Tyson is able to see that this is\n"
          "a binary star system. Before he can even take in the view the ship's\n"
          "scanners picks up 3 unknown planets, and a SOS signal...\n\n")
    time.sleep(5)

    print("Tyson:\n 'Why in the hell am I picking up a distress signal all the\n"
          "way out here. Besides the point I need to pick my next course of action.\n"
          "Even though the coordinates lead me here I thought it was suppose to be\n"
          "uncharted.'\n\n")
    time.sleep(2)
    choice1_chosen = 0
    while choice1_chosen == 0:
        choice1 = input("Tyson:\n\n'I can only think of 5 options:'\n\n"
                            "1. Respond to Distress Signal\n"
                            "2. Explore the closest planet(OMEGA-ZED-864)\n"
                            "3. Explore  the middle planet(OMEGA-ZED-865)\n"
                            "4. Explore the farthest planet(OMEGA-ZED-866)\n"
                            "5. Question the presence of SOS signal and\nengage hyperdrive to explore next star system.\n\n"
                            "Selection:")

        if choice1 == "1":
            print("Tyson:\n\n'This distress signal is the most important thing right now\n"
                  "Just why are there people here. If this place wasn't uncharted why\n"
                  "hide it? This seems like something I need to figure out on my own'\n\n")
            mc.choice1_chosen = 1
            print("Tyson sets the coordinates of the SOS signal into his ship and heads for it.\n\n")

            sosevent = random.randrange(1,3)            # This will set the variable randomly from either 1 to 3.

            if sosevent < 3:                    # If sosevent is less than 3 the ship will be hit by rocks.
                print("As you move towards the SOS signal the scanners start to blare, picking up multiple incoming\n"
                      "objects. You begin evasive maneuvers but there are too many objects. You engage the ships system\n"
                      "defenses and shoot some of the targets destroying them. Just as you get ready to make it through\n"
                      "the ship is hit my multiple objects causing significant damage to the ship. The sudden collision\n"
                      "caused Tyson to hit his head.\n\n")
                time.sleep(3)
                print("Tyson HP: -10")
                mc.tyson.healthpoints -= 10

            elif sosevent == 3:
                print("As you begin approaching the SOS signal you notice off in the distance through the window that\n"
                      "there is an astroid belt moving your way. Before the scanners can pick up the objects, Tyson\n"
                      "maneuvers the ship to avoid all incoming objects.\n\n")
                time.sleep(3)
            mc.chapter1_success = 1
            ACT2_THE_ONLY_HOPE.start()

# This elif statement is if the player chooses route 2. This will have the player try and check out the closest planet
# This will end up with the player taking some damage. (Can not explore planets yet)
        elif choice1 == "2":
            print("Tyson:\n\n'I think the best course of action is to survey these planets.\n"
                  "I'll start with the closest planet,OMEGA-ZED-864'\n\n")
            mc.choice1_chosen = 1

            #input()
            time.sleep(2)

            print("As Tyson begins his descent into the planet atmosphere he is\n"
                  "welcomed by a planet wide storm. As the ships descends deeper\n"
                  "into the storm Tyson notices that the it is raining some sort of\n"
                  "acidic liquid. Before he can react the ships alarm begins to blar\n "
                  "as the computer detects damage to the ship. Tyson hurries to take\n "
                  "control and takes the ship back into shape.\n\n")
            time.sleep(3)

            print("The acidic liquid has caused some breaches in the ship causing the ship to depressurize, causing some\n"
                  "damage to the Tyson.\n\n")
            print("Tyson's HP:", mc.tyson.healthpoints, "\n")
            time.sleep(1)
            mc.tyson.healthpoints -= 5
            print("Tyson's HP: -5\n")
            print("Tyson's HP:", mc.tyson.healthpoints, "\n\n")
            time.sleep(2)

            # oxygen = oxygen - 30

            # need to add a way for the player to be able to pick the options again.
# This is option #3 for the first option made by user. This choice will take the player to a planet you can not explore yet.
# The player will take some damage and will be sent back to orbit to make a new decision.
        elif choice1 == "3":
            print("Tyson:\n\n'I think the best course of action is to survey these planets.\n"
                  "I'll start with the middle planet OMEGA-ZED-865, I have a good feeling about this one.\n\n")
            mc.choice1_chosen = 1
            # input()
            time.sleep(2)

            print("All is okay as Tyson approaches the planet, but as he begins descending into the\n"
                  "planet's atmosphere he is met with an absolute bizarre situation. The ships\n"
                  "computer is reading extreme fluxuating temperatures. It is going from about absolute"
                  "zero to sun soarching temperatures.As Tyson goes deeper into the atmosphere the\n"
                  "alarms on the ship start to sound. The temperature changes are causing the ship to\n"
                  "malfunction. With the ships controls beginning to cease functions. Tyson engages the"
                  "atmospheric emergency protocol. The second this was activated, the ships thrusters\n"
                  "engaged and flew the ship out to open space.")
            #input()
            time.sleep(6)

            print("The ship took critical damage causing the air supply to momentarily turn off. As Tyson rushes\n"
                  "to grab his space suit he loses concinouses from a lack of oxygen, but wakes up moments later.")
            time.sleep(3)

            #print("Tyson's HP: -5")
            #mc.tyson.healthpoints -= 5
            print("Tyson's HP:", mc.tyson.healthpoints, "\n")
            time.sleep(1)
            mc.tyson.healthpoints -= 5
            print("Tyson's HP: -5\n")
            print("Tyson's HP:", mc.tyson.healthpoints, "\n\n")
            time.sleep(2)

            time.sleep(2)
            #oxygen = oxygen -25

            # need to add a way for the player to be able to pick the options again
# Option 4 for the first choice made by user. This will take you to a planet that you can not land on yet. The player
# takes some damage and is set back to space to make another decision.
        elif choice1 == "4":
            print("Tyson:\n\n'I think the best course of action is to survey these planets.\n"
                  "I'll start with the farthest planet OMEGA-ZED-866'\n\n")

            # input()
            time.sleep(2)
            print("As Tyson begins approaching the planet he notices multiple large burst\n"
                  "of purple light coming from the planet. Along with that ne notices a\n"
                  "black fog covering the planet. As he descends into the planet's atmosphere\n"
                  "he immediately notices the devices on the ship are starting to acting up. Before\n"
                  "he can react, the sky through the windows light up with huge streams of purple\n"
                  "lighting spanning the skyline. The intensity of the lighting keeps growing\n"
                  "until the ship is struck, and all controls are lost.\n\n"
                  "The ship starts flying uncontrollably into thick black fog. As the ship begins\n"
                  "spiralling out of control into an abyss, the ship crashes into something and\n"
                  "is not moving. As Tyson sits there thinking about his next move something grabs\n"
                  "the ship and begins moving it. Tyson is knocked to the floor and as he gets to his feet\n"
                  "he is confronted with what has to be an almost planetary sized creature.\n"
                  "It stares into your cockpit. The eye of this creature is as big as Tyson's ship begins\n"
                  "scanning every little detail before looking at Tyson and becomes visibly scared\n"
                  "hurling the ship back up into space.\n\n")
            time.sleep(5)
            print("Press enter when ready:")
            input()
            print("Tyson hits his head from the accident while the ship also takes some damage:\n"
                  "-10 health\n")         # Health and oxygen values will vary.
            input()
            mc.tyson.healthpoints -= 10
            print("Tyson's Health:", mc.tyson.healthpoints)
            time.sleep(4)

            # need to add a way for the player to be able to pick the options again

        # This option skips the other ACTS because when we jump to another star system we somehow end up at the star
        # system we would end up at the end of the story.
        elif choice1 == "5":
            print("Tyson:\n\n"
                  "'With there being some signs of life this can't be the place I was looking for.\n"
                  "I must keep searching. Ship plot course to closest uncharted area of space and\n"
                  "engage the hyperdrive.'\n\n")

            # mc.choice1_chosen = 1
            time.sleep(2)
            print("Tyson leaves this solar system in search for another. In hopes to find what he is\n"
                  "looking for.\n\n")
            time.sleep(2)

            print("Tyson's ship comes out of hyperspace at a new star system. So far the scanners have"
                  "picked up 1 planet and 1 unknown mass at the far edge of the solar system.\n\n\n")
            time.sleep(2)
            mc.cheater += 1

            print("Tyson:\n\n"
                  "'Now that I am here I can't detect any traces of life. I guess there are only 3 options:\n")
            choice2_chosen = 0      # To track choice while in new solar system
            while choice2_chosen == 0:          # Keeps letting the player
                choice2 = input("1.Explore the only planet(BETA-ZULU-101)\n"
                                "2.Explore unknown mass at edge of solar system\n"
                                "3.Go back to first solar system\n"
                                "Selection:\n")
                if choice2 == "1":
                    print("Tyson:\n\n"
                          "'I think the best course of action is to explore the planet (BETA-ZULU-101)")
                    time.sleep(2)
                    print("You begin your approach on the planet and notice nothing out of the ordinary when it\n"
                          "comes to the atmosphere and weather. The ship enters the atmosphere and as the ground\n"
                          "becomes visible you notice what seems like sprawling cities, but they are all\n"
                          "overgrown and void of any life besides the fauna. You notice a clearing a few miles\n"
                          "outside the city, and mark it as your landing destination.")
                    time.sleep(1)
                    print("Tyson:\n\n"
                          "'The scanners picked up no signs of any life, yet it seems that there was once a civilazation\n"
                          "here. None of this makes sense. Maybe I was at the right destination last time.\n\n")

                    time.sleep(1)
                    print("After exploring the the surrounding area of the landing site we find nothing of value.\n"
                          "However as you are walking back, you notice what seems like a bunker entrance. Out of\n"
                          "curisoity you break through the vault door. After a little bit of exploration you find\n"
                          "what seems to be a lab. You stumble into a chamber and the second you reach the center\n"
                          "the door behinds you closes and locks. As you begin to panick the power starts up and\n"
                          "the bunkers system begin operating. You hear a buzzing sound coming from above and see a\n"
                          "bright light beginning to form and starts getting brighter. You try to break out of the room by shooting\n"
                          "the door but no luck. The next thing you know you are being envoloped by a bright light and\n"
                          "pass out.\n\n ")
                    time.sleep(7)
                    print("When you come to, you find yourself laying on the ground with the door still closed. Not\n"
                          "knowing what happened you get frustrated and begin punching the door. As you continue to\n"
                          "punch the door your body begins to glow. As you next punch gets ready to connect with the\n"
                          "door a large burst of light gets emitted from your fist and the steel door is blown off\n"
                          "the hinges.\n\n")
                    time.sleep(2)
                    print("Having no idea what just happened, you rush back to the ship to get checked out by the ships\n"
                          "scanners. Once there you find out your body has been altered on a molecular level, giving\n"
                          "you super human abilites. This type of modification has never been seen before because\n"
                          "no biological life detected has the ability to withstand that amount of energy transfer.\n"
                          "Even the ships scanners had a hard time identifying what was going on. ")
                    time.sleep(1)
                    mc.inventory.append("COSMIC JUDGEMENT[CJ]")
                    mc.cs_check += 1
                    time.sleep(1)
                    print(mc.inventory)
                    time.sleep(2)

                    print("Tyson has decided he has had enough with this planet and decides to go back to space and\n"
                          "reevaluate his options.")
                    time.sleep(1)


                elif choice2 == "2":
                    print("Tyson:\n\n"
                          "'I have no idea what this mass could be, and with the scanners unable to identify it,\n"
                          "it has to be entity made structure.")
                    time.sleep(2)

                    print("Tyson heads for the structure at the far edge of the solar system.")
                    choice2_chosen += 1
                    # choice1_chosen += 1
                    ACT5_BRIDGE_TO_EVERYTHING.start()

                elif choice2 == "3":
                    print("You realize that you might be wrong on coming to this solar system and it does not match\n"
                          "the description you got from your previous hint. So you decide to go back to the orginal\n"
                          "solar system you were at.")
                    time.sleep(3)
                    choice2_chosen += 1

        else:
            print("Please Pick a valid input: '1, 2, 3, 4, 5'")
           # if choice2 == 1:
           #      print("")                      #This section will need to be added to.
           # elif choice2 == 2:
           #      print("")                      #This will lead to the end of the game
           #      input()
           #
           #      ACT5_BRIDGE_TO_EVERYTHING.start()
           #  elif choice2 == 3:
           #      print("")                      #Will take player back to first solar system and first options
           #
           #  else:
           #              #add way for choices to reappear if something else is pressed

















