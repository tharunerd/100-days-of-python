# understand if else statements
# This code is a simple text-based adventure game where the player makes choices to find a treasure

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision
choice1 = input("Left or right? ").strip().lower()
if choice1 != "left":
    print("Fall into a hole. Game Over.")
else:
    # Second decision
    choice2 = input("Swim or wait? ").strip().lower()
    if choice2 != "wait":
        print("Attacked by trout. Game Over.")
    else:
        # Third decision
        choice3 = input("thanks for waiting choose a door\nWhich door? Red, Blue or Yellow? ").strip().lower()
        if choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over.")


