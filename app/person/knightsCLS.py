from __future__ import annotations
from app.inventory.armour import Armour
from app.inventory.weapon import Weapon
from app.inventory.potion import Potion


class Knights:
    def __init__(self, name: str, power: int, hp: int,
                 armour_things: list,
                 weapon_thing: Weapon, potion_things: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour_things
        self.weapon = weapon_thing
        self.potion = potion_things
        self.protection = 0
        self.base_hp = hp
        self.base_power = power

    @classmethod
    def from_dict(cls, knights: dict) -> dict:
        objects = {}

        for knight, atr in knights.items():
            armours = [Armour(i["part"],
                              i["protection"]) for i in atr["armour"]]
            weapons = Weapon(atr["weapon"]["name"], atr["weapon"]["power"])
            if atr["potion"]:
                potions = Potion(atr["potion"]["name"],
                                 atr["potion"]["effect"])
            else:
                potions = None
            knight_obj = cls(name=atr["name"],
                             power=atr["power"],
                             hp=atr["hp"],
                             armour_things=armours,
                             weapon_thing=weapons,
                             potion_things=potions)
            objects[knight] = knight_obj

        return objects

    def prepare_for_battle(self) -> None:
        self.protection = 0
        self.hp = self.base_hp
        self.power = self.base_power
        for item in self.armour:
            self.protection += item.protection

        self.power += self.weapon.power

        if self.potion:
            effect = self.potion.effect

            if "hp" in effect:
                self.hp += effect["hp"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]

    def fight(self, enemy: Knights) -> dict:
        self.prepare_for_battle()
        enemy.prepare_for_battle()
        damage_to_enemy = max(0, self.power - enemy.protection)
        damage_to_self = max(0, enemy.power - self.protection)
        enemy.hp -= damage_to_enemy
        self.hp -= damage_to_self
        if enemy.hp < 0:
            enemy.hp = 0
        if self.hp < 0:
            self.hp = 0

        fighters = {self.name: self.hp, enemy.name: enemy.hp}
        self.end_battle()
        enemy.end_battle()
        return fighters

    def end_battle(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0
