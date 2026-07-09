class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Weapon:

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Knights:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: Weapon, potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0


def battle(knights: dict) -> dict:
    for knight in knights.values():
        knight["protection"] = sum(
            a["protection"] for a in knight["armour"])

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"]:
            for stat, value in knight["potion"]["effect"].items():
                knight[stat] = knight.get(stat, 0) + value
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    lancelot["hp"] = max(lancelot["hp"], 0)
    mordred["hp"] = max(mordred["hp"], 0)

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]
    arthur["hp"] = max(arthur["hp"], 0)
    red_knight["hp"] = max(red_knight["hp"], 0)

    return {
        lancelot["name"]: lancelot["hp"],
        mordred["name"]: mordred["hp"],
        arthur["name"]: arthur["hp"],
        red_knight["name"]: red_knight["hp"]
    }
