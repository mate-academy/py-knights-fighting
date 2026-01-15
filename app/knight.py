from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        self.power += knight["weapon"]["power"]

        for armour in knight["armour"]:
            self.protection += armour["protection"]

        if knight["potion"]:
            potion_effect = knight["potion"]["effect"]
            attributes = ["power", "protection", "hp"]

            for attribute in attributes:
                if attribute in potion_effect:
                    current_value = getattr(self, attribute)
                    setattr(
                        self,
                        attribute,
                        current_value + potion_effect[attribute]
                    )

    def fight_with(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
