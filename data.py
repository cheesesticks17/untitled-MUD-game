import shutil

SCREEN_WIDTH = shutil.get_terminal_size().columns

def create_player():
    """Walks the player through a set of prompts before creating the
    player character.
    """
    # Get name
    print("=" * SCREEN_WIDTH)
    print("Character Creation: ")
    print("=" * SCREEN_WIDTH)

    print("- Hello, unnamed individual, what is your name?")
    print("-" * SCREEN_WIDTH)

    name = input("> ")
    while name.isspace() or name is None:
        print("May I hear your name? ")
        name = input("> ")
    print(f"Alright! Hello {name}")
    return name    

def display(status: dict):
    """Takes in a status dict (returned by Game.status()) and formats
    it before displaying to user.
    """
    raise NotImplementedError


def prompt_player_choice(choices: list[str]):
    """Takes in list of choices, with each choice represented as a str,
    And displays them to the user for selection. The user is re-prompted
    If the choice is invalid. The player's choice is returned as a str.
    """
    # Displays choices
    print("- What will you do?")
    for i, choice in enumerate(choices, start = 1):
        print(f"  {i}. {choice}")
    print("-" * SCREEN_WIDTH)

    # Selection
    chosen_num = input("> ")
    while not chosen_num.isdigit() or int(chosen_num) < 1 or int(chosen_num) > len(choices):
        print(f"[!] Invalid input, chosen number should be within 1 and {len(choices)}")
        chosen_num = input("> ")

    return choices[chosen_num - 1]

    
