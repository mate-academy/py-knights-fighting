from typing import Any


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict[str, Any]],
        weapon: dict[str, Any],
        potion: dict[str, Any] | None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def from_config(cls, config: dict[str, Any]) -> "Knight":
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )

    def prepare_for_battle(self) -> None:
        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def _apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def _apply_potion(self) -> None:
        if self.potion is None:
            return

        for stat_name, effect_value in self.potion["effect"].items():
            current_value = getattr(self, stat_name)
            setattr(
                self,
                stat_name,
                current_value + effect_value,
            )

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        self.hp = max(0, self.hp - damage)
        
