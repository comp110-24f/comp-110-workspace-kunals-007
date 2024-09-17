"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730771282"


def input_word() -> str:
    """This function gathers a 5-character word input from the user."""
    user_input = input("Enter a 5-character word: ")
    if len(user_input) == 5:
        return user_input
    print("Error: Word must contain 5 characters.")
    exit()


def input_letter() -> str:
    """This function prompts the user for a single character."""
    user_input = input("Enter a single character: ")
    if len(user_input) == 1:
        return user_input
    print("Error: Character must be a single character.")
    exit()


def contains_char(word: str, letter: str) -> None:
    """Search for occurrences of the letter in the word and print the index."""
    print("Searching for " + letter + " in " + word)

    matches = 0
    index = 0

    # Loops through each index in the word
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            matches += 1
        index += 1

    # Print the number of matches found
    if matches == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(matches) + " instance(s) of " + letter + " found in " + word)


def main() -> None:
    """The main function to play Chardle."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
