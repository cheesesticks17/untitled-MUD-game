def create_player():
    """Walks the player through a set of prompts before creating the
    player character.
    """
    # Get name
    print("Hello, unnamed individual, what is your name?")
    name = input("> ")
    while name.isspace() or name is None:
        print("May I hear your name? ")
        name = input("> ")
    print(f"Alright! Hello {name}")


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
    raise NotImplementedError
