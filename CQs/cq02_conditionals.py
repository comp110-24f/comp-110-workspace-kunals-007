"""This function prompts a user to guess a randomly generated number and return if they were correct or not"""

__author__ = "730771282"


def guess_a_number() -> None:
    # This function determines whether a number inputted by the user matches the secret number
    secret: int = 7
    guess: int = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif guess > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return


if __name__ == "__main__":
    guess_a_number()
