import random


def get_secret_number():
    """Generate a random 3-digit number as a string"""
    return' '.join(str(random.randint(0,9))for _ in range(3))

def get_clues(guess,secret):
    """Return clues based on the guess"""

    if guess == secret:
        return "You got it!"

    clues =[]

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append("Fermi")
        elif guess[i] in secret:
            clues.append("Pico")
        if len(clues) == 0:
            return"Bagels"
        else:
            return"".join(clues)

def play_game():
            print("I am thinking of a 3-digit number.")
            print("Try to guess what it is.")
            print("clues.")
            print("Fermi -one number is correct and in the right position.")
            print("Pico -one number is correct but in the wrong positon.")
            print("Bagels -no nunmber is correct.")
            print("You have 10 guesses.\n")

            secret_number = get_secret_number()

            for guess_num in range(1,11):
                while True:
                    guess = input(f"Guess#{guess_num}:")
                    if len(guess)==3 and guess.isdigit():
                        break
                    print("Please enter valid 3-digit number.")

                    clues = get_clues(guess,secret_number)
                    print(clues)

                    if guess == secret_number:
                        break
                    else:
                        print(f"\nSorry,you ran out of guesses.The number was {secret_number}.")

                        play_again = input("\nDo you want to play again?(yes or no):").lower()
                    if play-again == "yes":
                            play_game()
                    else:
                             print("Thanks for playing!")



play_game()
                        
