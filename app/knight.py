from typing import Dict, Optional


class Knight:
    def __init__(self, data: Dict) -> None:
        self.name: str = data["name"]
        self.hp: int = data["hp"]
        self.power: int = data["power"]
        self.armour = data.get("armour", [])
        self.weapon = data.get("weapon", {})
        self.potion: Optional[Dict] = data.get("potion")

        self.protection: int = 0

        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        for piece in self.armour:
            self.protection += piece.get("protection", 0)

    def _apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def _apply_potion(self) -> None:
        if not self.potion:
            return

        effect = self.potion.get("effect", {})
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection

        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0
