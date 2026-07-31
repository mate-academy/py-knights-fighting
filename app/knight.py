from typing import Any


class Knight:
    def __init__(self, knight_data: dict[str, Any]) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(
            armour["protection"]
            for armour in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        for stat, value in self.potion["effect"].items():
            setattr(
                self,
                stat,
                getattr(self, stat) + value
            )
