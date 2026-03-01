from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp, armour, weapon, potion=None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = Knight.armour_sum(armour)
        self.weapon_buff(weapon)
        self.potion_effects(potion)


    @staticmethod
    def armour_sum(armour: list[dict]) -> int:
        defence = 0
        for piece in armour:
            defence += piece.get("protection", 0)
        return defence

    def power_changer(self, new_value: int) -> None:
        self.power += new_value

    def hp_changer(self, new_value: int) -> None:
        self.hp += new_value

    def armour_changer(self, new_value: int) -> None:
        self.armour += new_value

    def potion_effects(self, potion: dict | None) -> None:
        if not potion:
            return

        effects = potion.get("effect", {})
        if "hp" in effects:
            self.hp_changer(effects["hp"])
        if "power" in effects:
            self.power_changer(effects["power"])
        if "protection" in effects:
            self.armour_changer(effects["protection"])

    def weapon_buff(self, weapon):
        buff = weapon.get("power", 0)
        self.power_changer(buff)

    def battle(self, enemy:Knight) -> None:
        self.hp -= enemy.power - self.armour
        enemy.hp -= self.power - enemy.armour
        if self.hp <= 0:
            self.hp = 0
        if enemy.hp <= 0:
            enemy.hp = 0
