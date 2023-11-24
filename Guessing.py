import random

# List to store the number of attempts for each game played
attempts_list = []


def show_score():
    if not attempts_list:
        print("There's currently no high score. Start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")


def play_guessing_game():
    attempts = 0
    rand_number = random.randint(1, 10)

    print("Hello player! Welcome to the guessing game!")

    # Get player's name and whether they want to play
    player_name = input("What's your name? ")
    wanna_play = input(
        f"Hi, {player_name}, would you like to play the guessing game? Enter yes/no: "
    ).lower()

    # Exit the game if the player doesn't want to play
    if wanna_play == "no":
        print("That's cool, thanks!")
        exit()
    else:
        show_score()

    while wanna_play == "yes":
        try:
            # Get player's guess
            guess = int(input("Pick a number between 1 and 10: "))

            # Validate the guess
            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number between 1 and 10")

            attempts += 1

            # Check if the guess is correct
            if guess == rand_number:
                print("Nice, you got it!")
                print(f"It took you {attempts} attempts")

                # Ask if the player wants to play again
                wanna_play = input(
                    "Would you like to play again? Enter yes/no: "
                ).lower()

                # Update high score list
                attempts_list.append(attempts)

                # Exit the game if the player doesn't want to play again
                if wanna_play == "no":
                    print("That's cool, have a good day.")
                else:
                    # Reset attempts and generate a new random number for a new game
                    attempts = 0
                    rand_number = random.randint(1, 10)
                    show_score()
            elif guess > rand_number:
                print("It's lower!")
            else:
                print("It's higher!")
        except ValueError as err:
            print(err)


# Start the game
play_guessing_game()
