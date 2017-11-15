# A guessing game where the uzer has to guess a number between 1 and 100
# 11/12/17
# CTI-110 M6HW2 - Random number guessing game
# Brittani Alvarez



import random

guesses = 1

# Main function 

def main():
    again = "y"
    print("Let's play a guessing game!")
    print()

    # Loop for user to guess number

    while again.lower() == "y":
        play_game()
        again  = input("Do you want to play again? (y/n): ")
        print()
        
    print("Thanks for playing!")

# If and elif statment to tell if the guess is to high or too low

def play_game():
    number = random.randint(1, 100)
    count = 1

    while True:
        userGuess = int(input("Enter a number between 1 and 100: "))
        if userGuess > number:
            print("Your number is too high, try again.")
            count += 1

        elif userGuess < number:
            print("Your number is too low, try again.")
            count += 1

        elif userGuess == number:
            print("Congratulations! You guessed the right number in" , count, "guesses.")
            return 
        

# Call the main function
main()
