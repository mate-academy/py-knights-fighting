from __future__ import annotations


class Knight:
    def __init__(self, knight_params: dict) -> None:
        self.name = knight_params.get("name")
        self.power = knight_params.get("power")
        self.hp = knight_params.get("hp")
        self.armour = knight_params.get("armour")
        self.weapon = knight_params.get("weapon")
        self.potion = knight_params.get("potion")
        self.protection = 0

        for armour in self.armour:
            self.protection += armour.get("protection")

        self.power += self.weapon.get("power")

        if self.potion:
            for effect, value in self.potion.get("effect").items():
                setattr(self, effect, getattr(self, effect) + value)

    def attack(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        if self.hp < 0:
            self.hp = 0
