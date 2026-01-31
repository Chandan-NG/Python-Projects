print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Which direction would you go? Left or Right?")
direction = input("    Type 'Left' or 'Right'.\n").title()
if direction == "Left":
    print("You landed at an island. You want to cross the Sea.")
    motion= input("Do you want to wait for the boat or Swim?\n    Type 'Swim' or 'Wait'.\n").title()
    if motion == "Wait":
        print("You have three doors in front of you. Red, Yellow, Blue.")
        color = input("Which color door do you choose?\n    Type 'Red' or 'Yellow' or 'Blue'\n").title()
        if color == "Yellow":
            print("Congratulations! You win...!")
        elif color == "Red":
            print("Burned by Fire.\nGame Over...!")
        elif color=="Blue":
            print("Eaten by Beasts.\nGame Over...!")
        else:
            print("Game Over...!")
    else:
        print("Attacked by Trout\nGame Over...!")
else:
    print("You Fell into a hole.\nGame Over...!")
