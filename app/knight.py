from typing import Any


class Knight:
    def __init__(self, config: dict[str, Any]) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(
            item["protection"] for item in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        for stat, value in self.potion["effect"].items():
            setattr(self, stat, getattr(self, stat) + value)

    def receive_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)
