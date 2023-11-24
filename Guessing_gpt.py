import random

attempts_list = []


def show_score():
    if not attempts_list:
        print("there's  currently a high score, start plaing!")
    else:
        print(f"the current high score is {min(attempts_list)} attempts")


attempts = 0
rand_number = random.randint(1, 10)

print("Hello player! Welcome to the guessing game! ")

player_name = input("What's your name? ")
wanna_play = input(
    f"hi , {player_name}, would you like to play the guessing game? " "Enter yes/no: "
)

if wanna_play.lower() == "no":
    print("That's cool , thanks!")
    exit()
else:
    show_score()

while wanna_play.lower() == "yes":
    try:
        guess = int(input("pick a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            raise ValueError("please guess a number between 1 and 10")

        attempts += 1

        if guess == rand_number:
            print("Nice, you got it!")
            print(f"it took you {attempts} attempts")
            wanna_play = input("would you like to play again (enter yes/no): ").lower()

            attempts_list.append(attempts)

            if wanna_play == "no":
                print("that's cool , have a good day.")
            else:
                attempts = 0
                rand_number = random.randint(1, 10)
                show_score()
                continue
        elif guess > rand_number:
            print("it's lower!")
        else:
            print("it's higher!")
    except ValueError as err:
        print(err)
