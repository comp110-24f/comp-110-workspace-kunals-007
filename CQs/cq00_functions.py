"""
This function takes a message and returns (mimics) it right back to you.
"""

__author__ = "730771282"

def mimic(message: str) -> str:
    """
    This function returns the message inputted by the user
    
    Parameters:
        message (str): The message that is going to be mimicked
        
    Returns:
        str: The same message that was the input
    """
    return message

def main() -> None:
    """
    This function calls the mimic function with the user input and then prints the result
    
    Parameters:
        None

    Returns:
        None
    """
    print(mimic(message=input("What is your message?")))

if __name__ == "__main__":
    main()
