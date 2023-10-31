class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def add_armour(self, armours: list) -> None:
        for armour in armours:
            self.protection += armour["protection"]

    def add_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def add_potion(self, potion: dict) -> None:
        if "power" in potion["effect"]:
            self.power += potion["effect"]["power"]
        if "hp" in potion["effect"]:
            self.hp += potion["effect"]["hp"]
        if "protection" in potion["effect"]:
            self.protection += potion["effect"]["protection"]


def create_knight(knight: dict) -> Knight:
    result = Knight(
        name=knight["name"],
        power=knight["power"],
        hp=knight["hp"]
    )
    if knight["armour"]:
        result.add_armour(knight["armour"])

    result.add_weapon(knight["weapon"])

    if knight["potion"]:
        result.add_potion(knight["potion"])
    return result


def fight(knight: Knight, enemy: Knight) -> None:
    knight.hp -= enemy.power - knight.protection

    if knight.hp < 0:
        knight.hp = 0


def battle(knights_dict: dict) -> dict:
    knights = [
        create_knight(knight=knight[1])
        for knight in knights_dict.items()
        if knight[0] is not None
    ]
    for index in range(len(knights) - 2):
        fight(knights[index], knights[index + 2])
        fight(knights[index + 2], knights[index])

    return {knight.name: knight.hp for knight in knights}
