#------https://www.asciiart.eu/miscellaneous/dice
#http://xahlee.info/comp/unicode_games_cards.html
dicetype = ["""
  ____
 /\\\' .\\    _____
/: \\___\\  / .  /\\
\\\' / . / /____/..\\
 \\/___/  \\'  '\\  /
          \\'__'\\/
"""],["""
       _______
      /\ o o o\
     /o \ o o o\_______
    <    >------>   o /|
     \ o/  o   /_____/o|
      \/______/     |oo|
            |   o   |o/
            |_______|/
    
    
"""],[ """
       .-------.    ______
      /   o   /|   /\     \
     /_______/o|  /o \  o  \
     | o     | | /   o\_____\
     |   o   |o/ \o   /o    /
     |     o |/   \ o/  o  /
     '-------'     \/____o/

"""]


import sys
import time # for pause
import os #to clear the screen
#--------------------------Definition of the bikes------------------------------#
card1 = [0, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card2 = [1, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card3 = [2, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card4 = [3, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card5 = [4, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card6 = [5, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card7 = [6, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card8 = [7, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card9 = [8, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
card10 = [9, "motor1", ["HP", 100], ["Speed", 150], ["Engine capacity", 2000]]
cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10]
#--------------------------------dice throw-------------------------------------#
def dice():
    import random
    x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    return x1,x2
#-------------------------------clear screen-----------------------------------#
def clearscreen():
    os.system("cls" if os.name == "nt" else "clear") #clear screen
#-------------------------------------------------------------------------------#
def dicethrowanime():
    for i in range(len(dicetype)):

        clearscreen()
        print(dicetype[i])
        time.sleep(0.1)
    
#-------------------------------------------------------------------------------#
print("\nFirst player press enter to throw the dices:")
sys.stdin.readline()
dicethrowanime()
Player1Dice = dice()
clearscreen()
print("\n         Your results are : ")
print(Player1Dice[0], ' and ', Player1Dice[1])

