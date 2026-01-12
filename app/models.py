from typing import List, Optional, Dict


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: Dict[str, int]) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(self, name: str, base_power: int, hp: int,
                 armour: List[Armour],
                 weapon: Weapon,
                 potion: Optional[Potion]
                 ) -> None:
        self.name = name
        self.base_power = base_power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.power = self._calculate_total_power()
        self.protection = self._calculate_total_protection()
        self._apply_potion_to_hp()

    def _calculate_total_power(self) -> int:
        total_power = self.base_power + self.weapon.power
        if self.potion and "power" in self.potion.effect:
            total_power += self.potion.effect["power"]
        return total_power

    def _calculate_total_protection(self) -> int:
        total_prot = sum(item.protection for item in self.armour)
        if self.potion and "protection" in self.potion.effect:
            total_prot += self.potion.effect["protection"]
        return total_prot

    def _apply_potion_to_hp(self) -> None:
        if self.potion and "hp" in self.potion.effect:
            self.hp += self.potion.effect["hp"]

    def take_damage(self, damage: int) -> None:
        damage_to_deal = damage - self.protection
        if damage_to_deal < 0:
            damage_to_deal = 0

        self.hp -= damage_to_deal

        if self.hp < 0:
            self.hp = 0

    def fight(self, opponent: "Knight") -> None:
        opponent.take_damage(self.power)
