from __future__ import annotations


class Knight:

    def __init__(self, knight_dict: dict) -> None:
        self.knight_dict = knight_dict
        self.name = knight_dict["name"]
        self.power = knight_dict["power"]
        self.hp = knight_dict["hp"]
        self.protection = 0

    def __repr__(self) -> str:
        return f"Knight {self.name}: power = {self.power}, hp = {self.hp}," \
               f"protection = {self.protection}"

    def apply_extension(self) -> Knight:

        # apply armour
        for armour in self.knight_dict["armour"]:
            self.protection += armour["protection"]

        # apply weapon
        self.power += self.knight_dict["weapon"]["power"]

        # apply potion if exist
        if self.knight_dict["potion"] is not None:
            if "power" in self.knight_dict["potion"]["effect"]:
                self.power += \
                    self.knight_dict["potion"]["effect"]["power"]

            if "protection" in self.knight_dict["potion"]["effect"]:
                self.protection += \
                    self.knight_dict["potion"]["effect"]["protection"]

            if "hp" in self.knight_dict["potion"]["effect"]:
                self.hp += self.knight_dict["potion"]["effect"]["hp"]

        return self
