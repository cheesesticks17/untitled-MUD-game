class Player:
    def __init__(self, name: str):
        self.name = name
        self.max_health = 100
        self.health = self.max_health
        self.inventory = [] #size 5
        self.current_room = None
        self.attack = 1
    
    def get_data(self) -> list:
        data = []
        data.append(self.name)
        data.append(self.max_health)
        data.append(self.health)
        data.append(self.inventory)
        data.append(self.current_room)
        data.append(self.attack)

class Monster:
    def __init__(self, name: str, data: dict):
        self.name = name
        self.max_hp = data["Health"]
        self.hp = self.max_hp
        self.description = data["Description"]
        self.attack = data["Attack"]
        self.attack_message = data["Attack_Message"]
        self.defeat_message = data["Defeat_Message"]

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

class Items:
    
    def __init__(self, name: str, data: dict):
        self.name = name
        self.description = data["Descripton"]
        self.type = data["Type"]
        self.amount = data["Amount"]
        self.uses = data["Uses"]

    def consume(self, target):
        if self.type == "Healing":
            target.hp = min(target.max_health, target.health + self.amount)
        elif self.type == "Damage":
            target.attack += self.amount


class Room:
    def __init__(self, data: dict):
        self.name = data["Name"]
        self.description = data["Description"]
        self.exits = data["Exits"]
        self.creatures = []
        for creature, info in data["Creatures"]:
            self.creatures.append(Monster(creature, info))
        self.items = []
        for item, info in data["Items"]:
            self.item.append(Items(item, info))


class Maze:
    def __init__(self, rooms: dict, enemy: dict):
        self.rooms = {}
        for key, value in json.loads(rooms):
            self.rooms[key] = Room(value)
        self.current_room = self.rooms["Room 0"]
    
    def get_current_room(self) -> Room:
        return self.current_room
    
    def move_to_next_room(self, next_room: str) -> None:
        self.current_room = self.rooms[next_room]


    