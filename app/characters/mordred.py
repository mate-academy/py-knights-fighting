from __future__ import annotations


class Mordred:
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

    def get_ready(self) -> Mordred:
        self.get_armour()
        self.get_weapon()
        self.get_potion()
        return self


mordred_armour = [
    {
        "part": "breastplate",
        "protection": 15,
    },
    {
        "part": "boots",
        "protection": 10,
    }
]

mordred_weapon = {
    "name": "Poisoned Sword",
    "power": 60,
}

mordred_potion = {
    "name": "Berserk",
    "effect": {
        "power": +15,
        "hp": -5,
        "protection": +10,
    }
}

mordred = Mordred(
    name="Mordred",
    power=30,
    hp=90,
    armour=mordred_armour,
    weapon=mordred_weapon,
    potion=mordred_potion
)
