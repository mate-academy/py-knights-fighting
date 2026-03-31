from typing import Any


class Knight():
    def __init__(self, knight_data: dict[str, Any]) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.protection = 0
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]
        self._apply_armor()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armor(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def _apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def _apply_potion(self) -> None:
        if self.potion is not None:
            for stat_name, value in self.potion["effect"].items():
                current_value = getattr(self, stat_name)
                setattr(self, stat_name, current_value + value)

    def take_damage(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection
        self.hp = max(self.hp, 0)
