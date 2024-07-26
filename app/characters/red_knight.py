from __future__ import annotations


class RedKnight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict = None,
        protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def get_armour(self) -> None:
        self.protection = 0
        for elem in self.armour:
            self.protection += elem["protection"]

    def get_weapon(self) -> None:
        self.power += self.weapon["power"]

    def get_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def get_ready(self) -> RedKnight:
        self.get_armour()
        self.get_weapon()
        self.get_potion()
        return self


red_knight_armour = [
    {
        "part": "breastplate",
        "protection": 25,
    }
]

red_knight_weapon = {
    "name": "Sword",
    "power": 45
}

red_knight_potion = {
    "name": "Blessing",
    "effect": {
        "hp": +10,
        "power": +5,
    }
}


red_knight = RedKnight(
    name="Red Knight",
    power=40,
    hp=70,
    armour=red_knight_armour,
    weapon=red_knight_weapon,
    potion=red_knight_potion
)
