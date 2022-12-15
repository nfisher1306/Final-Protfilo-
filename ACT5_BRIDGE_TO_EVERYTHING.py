# Nikolas S Fisher
# Date:10/19/2022
#
# Description: The program will contain the code for the final act of this story.
# In this act the main character will be able to choose the final path for Tyson Barrel.
# Has the option to pick:
#      1.Go through gate, become all-powerful being (WIN)
#      2.Hit the redo button and live out a whole new life    (IDK yet maybe Win)
#      3.Finish you life and come back to still be a 'god' (Win)
#      4.Attack being. Die. Never become a 'god' (Game Over)
import time

import main_character as mc


def start():
    print("Act 5: 'The Bridge to Everything\n\n")
    time.sleep(3)

    print("After leaving the lighting planet, you lock in the coordinates and engage the hyperdrive..\n")
    time.sleep(2)
    print("Upon arriving at the coordinates you see a oddly shaped bridge with a massive portal at one end of it, and\n"
          "some chunk of land connected to the other end of the bridge.\n")
    print()
    print("As you get closer you notice some glowing entity hovering by the entrance to the bridge... It brings back a\n"
          "sense of familiarity but also a sense of fear.\n"
          "You are wary to land and circle the floating structure a few times before coming the decision to land.\n")
    time.sleep(3)
    print("When you land you notice no hostile intentions from the mysterious entity.")
    print()
    print("You exit the ship and approach the bridge and the entity.\n\n")
    time.sleep(3)
    print("After a few steps you hear a voice in your head calling out your name. After a second of panick you realize\n"
          "it is the voice of the glowing entity, as its gestures for you to come over.\n\n")

    print("GLOWING ENTITY:\n\n"
          "'For you have returned master.. once again.\n")
    print("TYSON:\n\n"
          "'What do you mean master and what do you mean once again I have never been here before..\n")
    print("GLOWING ENTITY:\n\n"
          "'Its only natural you do not remember these things, I should have known. But you are an\n"
          "all-powerful being that has the ability to transcend any reality, with the ability to\n"
          "transverse the multiverse. Create or destroy realities.\n")
    print("TYSON:\n\n"
          "'I... I..I need a second. to take this all in...\n")
    time.sleep(5)
    print("TYSON:\n\n"
          "'So you are telling me I am pretty much a god? If so then why would I decide to become some random person\n"
          "that can very much so die. The amount of times I have almosted died and shit myself is too many to count.\n")
    time.sleep(2)
    print("GLOWING ENTITY:\n\n"
          "'I guess you could say that, yes. You do these so called, 'evalutations' in differnt realities. You get rid\n"
          "of all your memories expect the mission which is to follow a step clues which explores all the universe has\n"
          "to offer. After follwoing all the clues you end up here...Its funny because you set this all up before you\n"
          "go anyways. So makes me wonder why you even wipe your memory in the first place.'\n")
    print("TYSON:\n\n"
          "'Well there is no way I am going to be able to understand or even gain a grasp on what you just said, but\n"
          "this place and you do feel all too familiar too me.'\n")
    time.sleep(3)
    if mc.cs_check >= 1:
        print("GLOWING ENTITY:\n"
              "'Master, now that I am taking a closer look at your body it seems that some of your powers has awaken\n"
              "in this form. I have never seen something like this happen before. What happened?'\n")
        time.sleep(3)
        print("TYSON:\n\n"
              "'I was actually in the planet in this star system and got stuck in some sort of chamber. After a bright\n"
              "light and passing out I came to and I had the ability to use some new mysterious power.'\n")
        time.sleep(2)
        print("GLOWING ENTITY:\n\n"
              "'I am amazed! Who would have thought that your power would be able to manifest in this body.. even if\n"
              "this is only a small fraction of your true power.\n\n")
        time.sleep(2)
    print("GLOWING ENTITY:\n\n"
          "'Well with that all begin said, what do you want to do? You can cross the bridge and go back to being a 'god'\n"
          "or you can start a new life, finish out the life of Tyson Barrel and come back when the time is right.\n"
          "Or you could start over again as a new life if you didn't think this was good enough.\n")
    # if mc.cs_check >= 1:
    #     print("GLOWING ENTITY:\n"
    #           "'Master, now that I am taking a closer look at your body it seems that some of your powers has awaken\n"
    #           "in this form. I have never seen something like this happen before. What happened?'")
    #     time.sleep(3)
    #     print("TYSON:\n\n"
    #           "'I was actually in the planet in this star system and got stuck in some sort of chamber. After a bright\n"
    #           "light and passing out I came to and I had the ability to use some new mysterious power.'")

    print("As much as you want to believe this entity you aren't too sure yet and still play it a little cautious.\n\n")

    bridgecheck = 0
    while bridgecheck == 0:
        choice1 = input("There are 4 options for you to pick from:\n"
                            "1. Don't trust the Glowing Entity and attack it.\n"            # Can win game if you win battle
                            "2. Hit the redo button and live out a new life\n"              # Technically lose but could end up here again in the new life
                            "3. Finish out life as Tyson Barrel\n"                          # WIN you just come back later when you decide to 
                            "4. Go through gate, go back to true form\n"                    # WIN you become a 'god'
                            "Selection:\n\n\n")

# This option will allow the player to attack the entity...
        if choice1 == "1":                            # LOSE        # if choice == 1 then this IF statement will run
            print("IDK why you would try to fight a god but hey you tired")
            AHchoice = 0
            combat5 = 0                                             # Variable to track when to end the fight
            while combat5 == 0:                                     # While loop to keep running these two functions
                while AHchoice == 0:
                    attack_heal = input("Please choice a option:\n"
                                        "1. Attack\n"
                                        "2. Heal\n"
                                        "Selection:")
                    if attack_heal == "1":

                        mc.glowguy.health = mc.attack(mc.glowguy.health)
                        AHchoice += 1
                        print("Tyson's HP:", mc.tyson.healthpoints)
                        print("GLOWING ENTITY:", mc.glowguy.health)
                        # if mc.tyson.healthpoints or mc.sp.health <= 0:
                        #     combat5 += 1
                        #     break

                    elif attack_heal == "2":
                        mc.tyson.healthpoints = mc.healing(mc.tyson.healthpoints, mc.glowguy.health)
                        AHchoice += 1
                        print("Tyson's HP:", mc.tyson.healthpoints)
                        print("GLOWING ENTITY:", mc.glowguy.health)

                if mc.tyson.healthpoints <= 0:
                    combat5 += 1


                mc.monster_attack(mc.tyson.healthpoints, mc.glowguy.entitynum)
                AHchoice -= 1
                if mc.glowguy.health <= 0:
                    combat5 += 1


                if mc.tyson.healthpoints <= 0:                      # checks whether player HP is 0 or less(if dead)
                    print("YOU HAVE DIED!")
                    print("You were unable to beat the glowing entity")
                    time.sleep(4)
                    print("You were so close.")
                    print("Only if you just walked across the bridge...")
                    exit()

                elif mc.glowguy.health <= 0:                        # Checks to see if entity is dead (HP is 0 or less)
                    print("By some miracle you beat a so called 'god'....")
                    print("You get yourself together and cross the bridge... as you enter the protal to the other side\n"
                          "you are greeted with the same face of the Glowing entity before... Before you can say a word\n"
                          "you are met with a punch and black out....")
                    time.sleep(3)
                    print("So did you end up as 'god' or did you fall back through the portal? I guess we will never know\n"
                          "since you decided to attack the thing in the first place!! It wasn't even trying to hurt you!\n\n")
                    time.sleep(3)
                    print("Congratulations! You have reached the end of the game!\n"
                          "FINAL CHOICE: Attack the entity...\n"
                          "Thank you for playing!")
                    time.sleep(4)
                    exit()
            # In this section there will be a combat part with the being
            # Beings Hit-Points = 1000
            # There will be a 30-50% chance your attack has no effect(only for conventional weapons)

# This IF statement is if choice1 equals 2, This will have the player chose to be reborn
        elif choice1 == "2":                          # Do not win
            print("GLOWING ENTITY:\n\n"
                  "'So you have decide to go around once more master? So be it... let me grant you your command. But\n"
                  "next time you make it back here there is no more games the realm needs you...'")
            time.sleep(4)
            print("Before you can get a word off the Entity teleports in front of you, touching your forehead. After\n"
                  "this everything go black..... who knows what story is to be had next.")
            time.sleep(3)

            print("Congratulations! You have reached the end of the game....\n"
                  "FINAL CHOICE: To be reborn...\n"
                  "Thank you for playing!!\n")
            time.sleep(5)
            exit()

# This IF statement checks to see if choice1 is equal to 3, if so it will run this section of code.

        elif choice1 == "3":                          # Do not win
            print("GLOWING ENTITY:\n\n"
                  "'Well master I do not blame you, you usually dont complete this quest so early on in your bodies\n"
                  "lifespan. When you get back, there is no waiting around the realm needs you...")
            time.sleep(3)
            print("Congratulations! You have reached the end of the game....\n"
                  "FINAL CHOICE: Finish life of Tyson Barrel\n"
                  "Thank you for playing!!\n")
            time.sleep(5)
            exit()

# This IF statement checks to see if choice1 is equal to 4, if so it will run this section of code.
# This is the chose that you want to pick!
        elif choice1 == "4":                          # WIN
            print("GLOWING ENTITY:\n\n"
                  "'You have made the right decision.. Let me walk you through, this process is rather unsettling for\n"
                  "you. In a split second you will understand the concept of every multiverse there every could be...\n"
                  "its a lot to take it.")
            time.sleep(3)
            print("You walk across the bridge and stand in front of the massive portal. You think back to all the\n"
                  "shit you had go through to reach this point and how you would do it all over again if you could.\n"
                  "Maybe walking in someones else shoes really does help you gain a a better understanding of their\n"
                  "perspective.")
            time.sleep(3)
            print("You take step through and everything turns to white, and when you open your eyes again you see\n"
                  "everything that ever was, is and will be. There is so much information to process, I couldn't\n"
                  "even begin to try ad explain it...\n")
            time.sleep(2)
            print("Congratulations! You have reached the end of the game....\n"
                  "FINAL CHOICE: To become a 'god'\n"
                  "Thank you for playing!!\n")
            time.sleep(5)
            exit()

# This else will for any other input other than the 4 desired ones. If not it wil run this check of code, letting the
# user that they need to enter a valid choice..
        else:                                       # Pick Again
            print("Invalid choice....\n")

            print("Please enter a valid input")

            time.sleep(1)
