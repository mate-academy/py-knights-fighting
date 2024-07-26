from __future__ import annotations


class Arthur:
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

    def get_ready(self) -> Arthur:
        self.get_armour()
        self.get_weapon()
        self.get_potion()
        return self


arthur_armour = [
    {
        "part": "helmet",
        "protection": 15,
    },
    {
        "part": "breastplate",
        "protection": 20,
    },
    {
        "part": "boots",
        "protection": 10,
    }
]

arthur_weapon = {
    "name": "Two-handed Sword",
    "power": 55,
}


arthur = Arthur(
    name="Arthur",
    power=45,
    hp=75,
    armour=arthur_armour,
    weapon=arthur_weapon
)
