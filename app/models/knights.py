from typing import Any


class Knight:
    def __init__(self, data: dict[str, Any]) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.armour = data["armour"]
        self.weapon = data["weapon"]
        self.potion = data["potion"]
        self.protection = 0

        self.prepare_for_battle()

    def apply_armour(self) -> None:

        self.protection = sum(item["protection"] for item in self.armour)

    def apply_weapon(self) -> None:

        self.power += self.weapon["power"]

    def apply_potion(self) -> None:

        if self.potion:
            for attr, value in self.potion["effect"].items():
                setattr(self, attr, getattr(self, attr) + value)

    def prepare_for_battle(self) -> None:

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def receive_damage(self, damage: int) -> None:

        self.hp = max(self.hp - damage, 0)

    def attack(self, opponent: "Knight") -> int:

        damage = max(self.power - opponent.protection, 0)
        opponent.receive_damage(damage)
        return damage
