"""This program asks the user for the number of guests to calculate the quantity of tea bags needed, the number of treats to accompany the tea, and the expected cost of the party."""

__author__: str = "730771282"


def main_planner(guests: int) -> None:
    """This function calls each function and produces printed output"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # This prints the number of guests the user asks for
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # This prints the number of tea bags required
    print(
        "Treats: " + str(treats(people=guests))
    )  # This prints the number of treats required
    print(
        "Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests)))
    )  # This prints the total cost to the user


def tea_bags(people: int) -> int:
    """This function determines number of tea bags needed based on number of guests"""
    return people * 2  # This gives each person 2 tea bags


def treats(people: int) -> int:
    """This function computes number of treats needed based on number of guests"""
    return int(tea_bags(people=people) * 1.5)  # This gives each person 1.5 treats


def cost(tea_count: int, treat_count: int) -> float:
    """This function computes the cost of the tea bags and the treats combined"""
    return (
        tea_count * 0.5 + treat_count * 0.75
    )  # This sums the cost of the tea and treats together


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
