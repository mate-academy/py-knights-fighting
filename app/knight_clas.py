from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: dict,
                 protection: int | None = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    @classmethod
    def from_dict(cls, config: dict) -> Knight:
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def protect(self) -> None:
        self.protection = 0
        for protection_one in self.armour:
            self.protection += protection_one["protection"]

    def before_fight(self) -> None:
        self.protect()
        self.apply_weapon()
        if self.potion is None:
            return
        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]
        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]
