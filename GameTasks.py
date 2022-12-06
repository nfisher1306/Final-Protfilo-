# Nikolas S Fisher
# 11/30/2022
#
#
#
#
#
#

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses


player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)


def task1(player): # needs rope, coat, and first aid kit, cannot have slow (climb mountain)
    if "rope" in player1.weapons and "coat" in player1.weapons and "first aid kit" in player1.weapons and "slow" \
            not in player1.weaknesses:
        return True

    else:
        return False


def task2(player):  # needs pan, groceries, cannot have small (cook meal)
    if "pan" in player1.weapons and "groceries" in player1.weapons and "small" not in player1.weaknesses:
        return True

    else:
        return False


def task3(player): # needs pen, paper, idea, cannot have confusion (write book)
    if "pen" in player1.weapons and "paper" in player1.weapons and "idea " in player1.weapons and "confusion" not in \
     player1.weaknesses:
        return True

    else:
        return False


print(task1(player1.weapons))


print(task2(player1.weapons))


print(task3(player1.weapons))