from __future__ import annotations


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.equipment = {"armour": [], "weapon": "", "potion": ""}
        print(f"Knight {name} arrived at the championship!")

    def add_armours(self, armours_list: list) -> None:
        for item in armours_list:
            if "part" in item.keys() and "protection" in item.keys():
                self.equipment["armour"].append(item["part"])
                self.protection += item["protection"]

    def add_potion(self, potion: dict) -> None:
        self.equipment["potion"] = potion["name"]
        effects = potion["effect"]
        if "power" in effects:
            self.power += effects["power"]
        if "hp" in effects:
            self.hp += effects["hp"]
        if "protection" in effects:
            self.protection += effects["protection"]

    def add_weapon(self, weapon: dict) -> None:
        self.equipment["weapon"] = weapon["name"]
        self.power += weapon["power"]

    def attack(self, opponent: Knight) -> None:
        opponent.hp -= max(0, self.power - opponent.protection)
        opponent.hp = max(0, opponent.hp)
