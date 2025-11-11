from typing import Dict, Any


class Knight:
    def __init__(self, knight_data: Dict[str, Any]) -> None:
        self.name = knight_data["name"]
        self.base_power = knight_data["power"]
        self.base_hp = knight_data["hp"]
        self.armour = knight_data.get("armour", [])
        self.weapon = knight_data["weapon"]
        self.potion = knight_data.get("potion")

        self.power = 0
        self.hp = 0
        self.protection = 0

        self._prepare_for_battle()

    def _prepare_for_battle(self) -> None:

        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0

        self._apply_armour()

        self._apply_weapon()

        self._apply_potion()

    def _apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def _apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def _apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]

            if "power" in effect:
                self.power += effect["power"]

            if "protection" in effect:
                self.protection += effect["protection"]

            if "hp" in effect:
                self.hp += effect["hp"]

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

    def is_defeated(self) -> bool:
        return self.hp <= 0

    def __repr__(self) -> str:
        return (f"Knight(name='{self.name}', "
                f"hp={self.hp}, power={self.power}, "
                f"protection={self.protection})")
