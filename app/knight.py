from __future__ import annotations


class Knight:
    def __init__(self, knight_information: dict) -> None:
        self.knight_information = knight_information
        self.name = knight_information.get("name")
        self.power = knight_information.get("power")
        self.hp = knight_information.get("hp")
        self.armour = knight_information.get("armour")
        self.weapon = knight_information.get("weapon")
        self.potion = knight_information.get("potion")
        self.protection = 0

    def apply_armour(self) -> None:
        for value1 in self.armour:
            for key, value in value1.items():
                if key == "protection":
                    self.protection += value

        self.knight_information.update({"protection": self.protection})

    def apply_weapon(self) -> None:
        for key, value in self.weapon.items():
            if key == "power":
                self.power += value

        self.knight_information.update({"power": self.power})

    def apply_potion(self) -> None:
        if self.potion is not None:
            for key, value in self.potion.items():
                if key == "effect":
                    for key2, item in value.items():
                        if key2 == "power":
                            self.power += item
                        if key2 == "protection":
                            self.protection += item
                        if key2 == "hp":
                            self.hp += item

        self.knight_information.update({"power": self.power})
        self.knight_information.update({"protection": self.protection})
        self.knight_information.update({"hp": self.hp})

    def __str__(self) -> str:
        return str(
            {key: value
             for key, value in self.knight_information.items()}
        )

    def update_hp(self, value: int) -> None:
        self.knight_information.update({"hp": value})

    def all_preparations(self) -> dict:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self.knight_information
