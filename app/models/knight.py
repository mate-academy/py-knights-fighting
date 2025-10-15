from __future__ import annotations


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_equipment(self) -> None:
        """Aplica efeitos de armadura, arma e poção."""
        # Armaduras
        self.protection = sum(a["protection"] for a in self.armour)

        # Arma
        self.power += self.weapon["power"]

        # Poção
        if self.potion:
            effects = self.potion["effect"]
            self.power += effects.get("power", 0)
            self.hp += effects.get("hp", 0)
            self.protection += effects.get("protection", 0)

    def attack(self, other: Knight) -> None:
        """Realiza ataque entre cavaleiros."""
        damage = self.power - other.protection
        other.hp = max(0, other.hp - damage)
