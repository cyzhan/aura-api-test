import random


def generator_1(num: int) -> str:
    """
    Converts a number between 1 and 5 to a specific string pattern.

    Args:
        num (int): An integer between 1 and 5.

    Returns:
        str: A formatted string based on the input number.
    """
    if not (1 <= num <= 5):
        return "Invalid input. Please enter a number between 1 and 5."

    # Generate the string based on the input number
    if num == 1:
        return str(random.randint(0, 9))
    elif num == 2:
        return f"{random.randint(0, 9)},{random.randint(0, 9)}"
    elif num == 3:
        return f"{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)}"
    elif num == 4:
        return f"{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)}"
    elif num == 5:
        return f"{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)}"
