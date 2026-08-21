class Player:
        def __init(self, name: str, ):
            self.name = name
            self.health = 100
            self.max_health = 100
            self.inventory = [] #size 5
            self.current_room = None

    class Monster:
        def __init__(self):
            self.hp = 100
            self.max_hp = 100
            self.speed = 1 #undecided
            self.attack = 5

        def check_alive(self) -> bool:
            if self.hp <= 0:
                return False
            return True

        def get_hp(self) -> int:
            return self.hp

        def set_hp(self, new_hp: int) -> None:
            self.hp = new_hp

        def get_attack(self) -> int:
            return self.attack

        def set_attack(self, new_attack: int) -> None:
            self.attack = new_attack

        def take_damage(self, damage: int) -> None:
            """Entity suffers damage"""
            self.hp -= damage
    

    class Items:
        
        def __init__(self):
            self.name = "Placeholder"
            self.description = "Placeholder"
            self.heal = None
            self.attack_buff = None
            self.vunerability = None
            self.open_the_portal = False
        
    class Room:
        def __init__(self, name: str, description: str, exits: dict, creatures: list, items: list):
            self.name = name
            self.description = description
            self.exits = exits
            self.creatures = creatures
            self.items = items

    class Maze:
        def __init__(self):
            self.rooms = []
            self.start_room = Room()
            self
        
