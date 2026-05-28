from app.knights.components import Weapon, ArmourPart, Potion


class Knight:
    def __init__(self, raw_data: dict) -> None:
        self.name: str = raw_data["name"]
        self._base_hp: int = raw_data["hp"]
        self._base_power: int = raw_data["power"]

        self.weapon = Weapon(raw_data["weapon"])
        self.armour = [ArmourPart(part) for part in raw_data["armour"]]
        self.potion = Potion(raw_data["potion"])

        self.hp: int = self._calculate_hp()
        self.power: int = self._calculate_power()
        self.protection: int = self._calculate_protection()

    def _calculate_hp(self) -> int:
        return self._base_hp + self.potion.hp_effect

    def _calculate_power(self) -> int:
        return self._base_power + self.weapon.power + self.potion.power_effect

    def _calculate_protection(self) -> int:
        total_armour_protection = sum(part.protection for part in self.armour)
        return total_armour_protection + self.potion.protection_effect

    def take_damage(self, opponent_power: int) -> None:
        """Reduces the knight's health based
         on the enemy's attack and defense"""
        actual_damage = opponent_power - self.protection

        if actual_damage > 0:
            self.hp -= actual_damage

        if self.hp < 0:
            self.hp = 0
