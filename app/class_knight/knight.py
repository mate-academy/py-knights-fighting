from __future__ import annotations


class Knight:

    def __init__(
            self, name: str,
            power: int, hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def prepare(name: str, knights_config: dict) -> Knight:
        knight_dict = knights_config[name]
        current_knight = Knight(knight_dict["name"], knight_dict["power"],
                                knight_dict["hp"], 0)
        if len(knight_dict["armour"]) > 0:
            for armour in knight_dict["armour"]:
                current_knight.protection += armour["protection"]
        current_knight.power += knight_dict["weapon"]["power"]
        if knight_dict["potion"]:
            current_knight.power += knight_dict["potion"]["effect"]["power"]
            current_knight.hp += knight_dict["potion"]["effect"]["hp"]
            if knight_dict["potion"]["effect"].get("protection", None):
                current_knight.protection += \
                    knight_dict["potion"]["effect"]["protection"]
        return current_knight
