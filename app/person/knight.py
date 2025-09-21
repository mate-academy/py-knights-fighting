from app.person.config import KNIGHTS


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0


def creator(config_file: dict) -> dict:
    persons = {}
    for key, value in config_file.items():
        persons[key] = Knight(name=value["name"],
                              power=value["power"],
                              hp=value["hp"],
                              armour=value["armour"],
                              weapon=value["weapon"],
                              potion=value["potion"])
    return persons


if __name__ == "__main__":
    print(creator(KNIGHTS))
