import random


colok_jitu_options = ["AS", "KOP", "KEPALA", "EKOR"]

def four_three_two_d(num: int) -> str:
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


def colok(bet_option: str) -> str:
    if bet_option == "COLOK_BEBAS":
        return str(random.randint(0, 9))
    elif bet_option == "COLOK_MACAU":
        d1 = random.randint(0, 9)
        while True:
            d2 = random.randint(0, 9)
            if d1 != d2:
                return f"{d1},{d2}"
    elif bet_option == "COLOK_NAGA":
        d1 = random.randint(0, 9)
        d2 = None
        while True:
            d2 = random.randint(0, 9)
            if d1 != d2:
                break
        while True:
            d3 = random.randint(0, 9)
            if d3 != d1 and d3 != d2:
                return f"{d1},{d2},{d3}"
    elif bet_option == "COLOK_JITU":
        d = random.randint(0, 9)
        return  f"{d},{colok_jitu_options[random.randint(0,3)]}"

