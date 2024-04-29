from __future__ import annotations

from app.items.item import Item


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            inventory: list[Item],
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.inventory = inventory
        self.protection = protection
        self.prepare_for_battle()

    @classmethod
    def create_from_dict(cls, player: dict) -> Knight:
        name = player["name"]
        power = player["power"]
        hp = player["hp"]
        inventory = [
            Item.create_from_dict("armour", armour)
            for armour in player["armour"]
        ]
        if player["weapon"]:
            inventory.append(Item.create_from_dict("weapon", player["weapon"]))
        if player["potion"]:
            inventory.append(Item.create_from_dict("potion", player["potion"]))
        return cls(name, power, hp, inventory)

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, value)

    def equip(self, item: Item) -> None:
        self.power += item.power
        self.hp += item.hp
        self.protection += item.protection

    def prepare_for_battle(self) -> None:
        for item in self.inventory:
            self.equip(item)
