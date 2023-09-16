from __future__ import annotations


class Knight:
    instances = {}

    def __init__(
            self,
            knight_name: str,
            knight_data: dict
    ) -> None:
        self.name = knight_data.get("name")
        self.power = knight_data.get("power", 0)
        self.hp = knight_data.get("hp", 0)
        self.armour = knight_data.get("armour", [])
        self.weapon = knight_data.get("weapon", {})
        self.potion = knight_data.get("potion", None)
        self.protection = 0
        Knight.instances[knight_name] = self

    def apply_armour(self) -> None:
        for current_armour in self.armour:
            self.protection += current_armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            for attribute in ["power", "protection", "hp"]:
                if attribute in effect:
                    current_value = getattr(self, attribute)
                    setattr(self, attribute, effect[attribute] + current_value)

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp <= 0:
            self.hp = 0

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion_if_exist()
