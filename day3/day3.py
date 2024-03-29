print(
    '''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Write your code below this line 👇
choice1 = input("You're at a crossroad. Where do you want to go? left or right: ").lower()
if choice1 == "left":
    print("You fell into a hole and found a door with 3 colors: Red, Blue, Yellow.")
    choice2 = input("Which color do you choose? ").lower()
    if choice2 == "yellow":
        print("You got burned by fire. Game Over.")
    elif choice2 == "blue":
        print("You got eaten by beasts. Game Over.")
    else:
        choice3 = input("Which key do you choose: the golden one or the silver one? ").lower()
        if choice3 == "golden":
            print("Congratulations! You found the treasure! You win!")
        else:
            print("The key exploded and you died. Game Over.")
else:
    print("You went into a lake and got eaten by a monster. Game Over.")
