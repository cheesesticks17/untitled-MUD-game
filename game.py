import model
    

class Game:
    """Encapsulates the game logic, excluding room and character data.
    """

    def __init__(self):
        self.play_area = Maze()
        self.player = None
        self.game_over = False
        self.status = "alive"


    def add_player(self, name: str) -> None:
        """Adds the player into the game.
        Only one player is supported for now.
        Raises an error if more than one player is added.
        """
        if self.player != None:
            raise error
        else:
            self.player = model.Player(name)
    

    def is_gameover(self) -> bool:
        """Returns True when the game should end, otherwise False."""
        return self.game_over


    def attack(self, predator, victim) -> None:
        """guy attack guy"""
        victim.set_hp(victim.get_hp() - predator.get_attack())
        if not victim.check_alive():
            if victim == self.player:
                self.game_over = True
            else:
                del self.play_area.current_room.creatures[victim.name]
            

    def traverse(self, target: str) -> bool:
        """travel to another room"""   
        if target in self.play_area.rooms:
            self.play_area.move_to_next_room(target)
            return True
        else:
            return False
    
    def get_options(self) -> list:
        """Generates a list of choices that player can make.
        Each choice is represented as a str.
        """
        options = []
        for creature in self.play_area.current_room.creatures: #list
            options.append("Attack " + creature.name)
        for item in self.play_area.current_room.items: #list
            options.append("Pick Up " + item.name)
        for path in self.play_area.current_room.exits: # dict
            options.append("Go " + path)
        if len(self.player.inventory) <= 4:
            for item in self.player.inventory:
                options.append("Use " + name)
        chosen = data.prompt_player_choice(options)
        return options[chosen]
    
    def execute(self, choice: str) -> None:
        if "Attack " in choice:
            for creature in self.play_area.current_room.creatures:
                if creature.name in choice:
                    self.attack(self.Player, creature)
        elif "Use " in choice:
            for i in range(len(self.player.inventory)):
                if self.player.inventory[i].name in choice:
                    self.player.inventory[i].consume(self.player)
                    if self.player.inventory[i] <= 0:
                        self.player.inventory.pop(i)
        elif "Pick Up "in choice:
            for item in self.play_area.current_room.items:
                if item.name in choice:
                    self.player.inventory.append(item)
        else:
            self.traverse(choice[3:])


    def get_status(self) -> dict:
        return self.player.get_data()
        

    def welcome(self) -> None:
        """Displays the welcome message for the start of the game."""
        print("Welcome to Sample Game!")
        print("=======================")


def epilogue() -> None:
    """Displays the game epilogue."""
    print("==================================")
    print("Thank you for playing Sample Game!")
