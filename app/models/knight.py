from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def _apply_armour(self, armour: list[dict]) -> None:
        for piece in armour:
            self.protection += piece["protection"]

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return

        effect = potion["effect"]
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def take_damage(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection
        if self.hp <= 0:
            self.hp = 0

    @classmethod
    def from_dict(cls, knight_dict: dict) -> Knight:
        knight = cls(
            name=knight_dict["name"],
            power=knight_dict["power"],
            hp=knight_dict["hp"],
        )
        knight._apply_armour(knight_dict["armour"])
        knight._apply_weapon(knight_dict["weapon"])
        knight._apply_potion(knight_dict["potion"])
        return knight
