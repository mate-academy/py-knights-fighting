from __future__ import annotations


class KnightBasic:

    def __init__(self, knight: dict) -> None:

        # basic attributes
        self.protection = 0
        self.hp = knight.get("hp")
        self.name = knight.get("name")
        self.power = knight.get("power")
        self.weapon = knight.get("weapon")

        # additional attributes
        self.armour = knight.get("armour")
        self.potion = knight.get("potion")

    def battle_preparing(self) -> None:
        # take weapon to arms
        self.power += self.weapon["power"]

        # wear armour if you have one
        if self.armour:
            for equip in self.armour:
                self.protection += equip["protection"]

        # drink potion if you have one
        if self.potion:
            for effect, value in self.potion.get("effect").items():
                # Using getattr and setattr to dynamically update attributes
                if hasattr(self, effect):
                    setattr(self, effect, getattr(self, effect) + value)
