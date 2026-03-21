# from datafile import data
# import random
#
# def higherlower():
#     option_a = random.choice(data)
#     option_b = random.choice(data)
#     if  option_a == option_b:
#         option_b = random.choice(data)
#
#     score = 0
#     continue_game = True
#
#     while continue_game:
#         print(f"\nCompare A: {option_a['name']} ")
#         print("VS")
#         print(f"Against B: {option_b['name']} ")
#
#         # Get user's guess
#         guess = input("Who has more searches? Type 'A' or 'B': ").strip().upper()
#
#         if option_a["searches"] > option_b["searches"]:
#             correct_answer = "A"
#         else:
#             correct_answer = "B"
#
#         if guess == correct_answer:
#             score += 1
#             print(f"You're right! Current score: {score}")
#             # Replace the losing option with a new random item
#             if correct_answer == "A":
#                 option_b = random.choice(data)
#             else:
#                 option_a = random.choice(data)
#                 if option_a == option_b:
#                     option_b = random.choice(data)
#         else:
#             print(f"Wrong answer! Your final score is: {score}")
#             continue_game = False
#
# higherlower()


from datafile import data
import random

def get_random_option(exclude=None):
    """Returns a random option from data, ensuring it's not the same as the excluded option."""
    option = random.choice(data)
    while option == exclude:
        option = random.choice(data)
    return option

def higherlower():
    option_a = get_random_option()
    option_b = get_random_option(option_a)

    score = 0
    continue_game = True

    while continue_game:
        print(f"\nCompare A: {option_a['name']} ")
        print("VS")
        print(f"Against B: {option_b['name']} ")

        # Get user's guess
        guess = input("Who has more searches? Type 'A' or 'B': ").strip().upper()
        while guess not in ["A", "B"]:
            print("Invalid input! Please enter 'A' or 'B'.")
            guess = input("Who has more searches? Type 'A' or 'B': ").strip().upper()

        correct_answer = "A" if option_a["searches"] > option_b["searches"] else "B"

        if guess == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}")

            # The correct choice remains; replace the other one
            if correct_answer == "A":
                option_b = get_random_option(option_a)
            else:
                option_a = get_random_option(option_b)
        else:
            print(f"Wrong answer! Your final score is: {score}")
            continue_game = False

higherlower()
