from __future__ import annotations


class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.hp = knight_config["hp"]
        self.power = knight_config["power"]
        self.protection = 0

        self.armour = knight_config["armour"]
        self.weapon = knight_config["weapon"]
        self.potion = knight_config["potion"]

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, health_points: int) -> None:
        self._hp = max(0, health_points)

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for effect in self.potion["effect"]:
                new_value = (
                    getattr(self, effect)
                    + self.potion["effect"][effect]
                )
                setattr(self, effect, new_value)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()

        self.apply_potion()

    @staticmethod
    def battle(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.prepare_for_battle()
        knight_2.prepare_for_battle()

        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
