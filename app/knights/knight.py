from .equipment import Armor, Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armor: list,
        weapon: Weapon,
        potion: Potion = None
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.stats = self.calculate_initial_stats()

    def calculate_initial_stats(self) -> dict:
        stats = {
            "power": self.base_power + self.weapon.power,
            "hp": self.base_hp,
            "protection": sum(
                [armor.protection for armor in self.armor]
            )
        }
        if self.potion:
            stats = self.potion.apply_effect(stats)
        return stats

    def receive_damage(self, damage: int):
        self.stats["hp"] -= damage
        if self.stats["hp"] < 0:
            self.stats["hp"] = 0
