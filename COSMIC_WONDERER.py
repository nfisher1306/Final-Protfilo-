# Nikolas S Fisher
# Date: 10/19/2022
#
# Description: This will have the entire story in here. The narrative etc..
# Overall I like what I have so far when it comes to story, however how I want to express the beginning is undecided.
# I want people to think they are playing some mysterious person that has experienced countless things. Other than that
# I can not think of anything else I want to add at the moment (11/2/2022)
#
#
#

import main_character
import ACT1_SOS
import ACT2_THE_ONLY_HOPE
import ACT3_THE_DWELLING_CITY
import ACT4_THE_TEMPLE_OF_THE_GODS
import ACT5_BRIDGE_TO_EVERYTHING
import time

main_character.init_glabal_vars()

print("Welcome to my game, 'Cosmic Wanderer'.\nI am excited to share this story with you.\n\n"
      "Please press ENTER to continue...",)
input()

print("Background:\nTyson Barrel AKA The Cosmic Wanderer is a lone traveler\n"                      
      "that is drifting through the stars in order to find the answer to\n"
      "interdimensional travel to get back home. After countless decades of\n"
      "searching he Tyson has narrowed down the last clue to an uncharted\n"
      "solar system where the paranormal is normal.\n\n\n")


time.sleep(4)
print("Game Objective:\nIn order to transverse the harsh climates of space\n"
      "Tyson need to collect the necessary gear and information to achieve\n"
      "his goal. But will it be so clean cut? This is uncharted territory\n"
      "there could anything in the shadows...\n\n\n")
time.sleep(4)
print("Tyson:\n'I have almost every last piece of the map leading to the\n"
      "gateway. The last corner of the universe I search is bringing to\n"
      "god knows where. This place isn't even chartered. Who knows\n"
      "there might be nothing hahaha. This last piece better be here\n"
      "I didn't do all those things for nothing.... Computer set\n"
      "coordinates and initiate hyperdrive.'\n\n\n")
time.sleep(4)

ACT1_SOS.start()
