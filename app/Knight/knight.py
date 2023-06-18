from __future__ import annotations
import time


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def apply_armour(self, armours: list[dict]) -> None:

        if armours:
            for armour in armours:
                print(f"Put on the {armour.get('part')}")
                time.sleep(0.5)
                self.protection += armour.get("protection")

    def apply_weapon(self, weapon: dict) -> None:
        print(f"Take the {weapon.get('name')}")
        time.sleep(0.5)
        self.power += weapon.get("power")

    def apply_potion(self, potion: dict) -> None:
        if potion:
            print(f"Apply {potion.get('name')}")
            time.sleep(0.5)
            effect = potion.get("effect")
            self.hp += effect.get("hp")
            self.power += effect.get("power")
            if protection := effect.get("protection"):
                self.protection += protection

    def equip_knight(
            self,
            armour: list[dict],
            weapon: dict,
            potion: dict
    ) -> None:
        print(f"----------Equip {self.name}----------")
        time.sleep(0.5)
        self.apply_armour(armour)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def battle_between_two(self, other: Knight) -> dict:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        return {
            self.name: self.hp if self.hp >= 0 else 0,
            other.name: other.hp if other.hp >= 0 else 0
        }
