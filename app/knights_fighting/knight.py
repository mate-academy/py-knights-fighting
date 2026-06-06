from app.knights_fighting.armour import Armour
from app.knights_fighting.poison import Poison
from app.knights_fighting.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armours: list[Armour] | None = None,
                 weapon: Weapon | None = None,
                 poisons: list[Poison] | None = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        self.armours = []
        self.weapon = weapon
        self.poisons = []

        if armours:
            for armour in armours:
                self.apply_armour(armour)
        if poisons:
            for poison in poisons:
                self.apply_poison(poison)
        if weapon:
            self.apply_weapon(weapon)

    def apply_armour(self, armour: Armour) -> None:
        self.armours.append(armour)
        self.protection += armour.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        if self.weapon is not None:
            self.power -= self.weapon.power
        self.weapon = weapon
        self.power += weapon.power

    def apply_poison(self, poison: Poison) -> None:
        self.poisons.append(poison)
        if poison.hp_affect:
            self.hp += poison.hp_affect
        if poison.power_affect:
            self.power += poison.power_affect
        if poison.protection_affect:
            self.protection += poison.protection_affect

    def prepare(self,
                weapon_data: dict,
                armours_data: list[dict],
                poison_data: dict | None) -> None:
        for armour_data in armours_data:
            self.apply_armour(
                Armour(armour_data["part"], armour_data["protection"])
            )
        self.apply_weapon(Weapon(weapon_data["name"], weapon_data["power"]))
        if poison_data is not None:
            self.apply_poison(Poison(
                poison_data["name"],
                poison_data["effect"].get("hp"),
                poison_data["effect"].get("power"),
                poison_data["effect"].get("protection")
            ))
