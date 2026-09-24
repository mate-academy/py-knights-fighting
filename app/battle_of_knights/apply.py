from __future__ import annotations


class Knight:
    def __init__(self, knight_dict: dict) -> None:
        self.knight_dict = knight_dict
        self.name = knight_dict["name"]
        self.power = self.calc_power()
        self.armour = self.calc_protection()
        self.hp = self.calc_hp()

    def calc_power(self) -> int:
        potion_power = self.get_potion_effect("power")
        return (
            self.knight_dict.get("power")
            + self.knight_dict["weapon"]["power"]
            + potion_power
        )

    def calc_protection(self) -> int:
        potion_protection = self.get_potion_effect("protection")
        armour_protection = 0

        if self.knight_dict["armour"]:
            armour = self.knight_dict.get("armour")
            for arm in armour:
                armour_protection += arm["protection"]
        return potion_protection + armour_protection

    def calc_hp(self) -> int:
        potion_hp = self.get_potion_effect("hp")
        return potion_hp + self.knight_dict["hp"]

    def get_potion_effect(self, stat_name: str) -> int:
        effect_value = 0
        potion = self.knight_dict.get("potion")
        if potion and stat_name in potion["effect"]:
            effect_value = potion["effect"].get(stat_name)
        return effect_value

    def fight(self, damage: int) -> None:
        self.hp = max(0, (self.hp - (damage - self.armour)))
