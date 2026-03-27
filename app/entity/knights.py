from __future__ import annotations


class Knights:
    def __init__(self, name: str, power: int, health: int) -> None:
        self.protection = 0
        self.power = power
        self.name = name
        self.health = health

    def apply_armor(self, armors: list) -> None:
        for armor in armors:
            self.protection += armor["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        for effects in potion["effect"]:
            if effects == "hp":
                self.health += potion["effect"]["hp"]

            if effects == "power":
                self.power += potion["effect"]["power"]

            if effects == "protection":
                self.protection += potion["effect"]["protection"]

    @staticmethod
    def init_knight(name: str, knights: dict) -> Knights:
        if name not in knights:
            raise ValueError

        result = Knights(
            name=knights[name]["name"],
            power=knights[name]["power"],
            health=knights[name]["hp"],
        )

        if knights[name].get("armour"):
            result.apply_armor(knights[name]["armour"])

        if knights[name].get("weapon"):
            result.apply_weapon(knights[name]["weapon"])

        if knights[name].get("potion"):
            result.apply_potion(knights[name]["potion"])

        return result

    def status(self) -> dict:
        return {self.name: self.health}

    def __repr__(self) -> str:
        return (f"Knight {self.name}: Power={self.power}, "
                f"Health={self.health}, Protection={self.protection}")
