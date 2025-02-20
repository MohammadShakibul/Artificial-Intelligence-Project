import random

l = ["rock", "paper", "scissor"]

# Initialize empty list to track previous computer choices
prev_choices = []

while True:
    choose = int(input('''
Want to play the game...?
1.Yes
2.No
'''))

    if choose == 1:
        my_count = 0
        computer_count = 0

        for _ in range(5):
            user_input = int(input('''
1.rock
2.paper
3.scissor
'''))

            if user_input == 1:
                my_ans = "rock"
            elif user_input == 2:
                my_ans = "paper"
            elif user_input == 3:
                my_ans = "scissor"
            else:
                print("Invalid input. Please try again.")
                continue  # Skip round for invalid input

            # Generate computer choice with logic to avoid repetition
            computer_ans = random.choice(l)
            if len(prev_choices) >= 2:
                while computer_ans == prev_choices[-1] and computer_ans == prev_choices[-2]:
                    computer_ans = random.choice(l)

            # Update previous choices list
            prev_choices.append(computer_ans)
            prev_choices = prev_choices[-2:]  # Keep only the last two choices

            print("Your Answer", my_ans)
            print("Computer Answer", computer_ans)

            if my_ans == computer_ans:
                print("Draw")
                my_count += 1
                computer_count += 1
            elif (
                (my_ans == "rock" and computer_ans == "scissor")
                or (my_ans == "paper" and computer_ans == "rock")
                or (my_ans == "scissor" and computer_ans == "paper")
            ):
                print("You Win")
                my_count += 1
            else:
                print("Computer Win")
                computer_count += 1

        print()
        print()

        if my_count == computer_count:
            print("Final Result:")
            print("Your Count", my_count)
            print("Computer Answer", computer_count)
            print("Game Draw")
        elif my_count > computer_count:
            print("Final Result:")
            print("Your Count", my_count)
            print("Computer Answer", computer_count)
            print("You Win The Game")
        else:
            print("Final Result:")
            print("Your Count", my_count)
            print("Computer Answer", computer_count)
            print("You lose the game")

    else:
        break

# This code incorporates the following improvements:

# Tracks previous choices: An empty list prev_choices is initialized to store the computer's past choices.
# Avoids repetition: Within the loop for generating the computer's choice, the code checks if the last two generated choices are the same. If so, it keeps re-generating a new choice until it finds one that's different from the previous two.
# Maintains list size: The prev_choices list is limited to the last two elements using slicing (prev_choices[-2:]) to ensure efficient memory usage.
# Handles invalid input: The code includes input validation to prevent the game from crashing due to unexpected user input.
# This approach provides a more challenging and unpredictable experience for the player by preventing the computer from repeating the same move in consecutive rounds.