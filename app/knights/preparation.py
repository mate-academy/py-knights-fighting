class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list | None,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def is_no_health(self) -> bool:
        if self.hp <= 0:
            self.hp = 0
            return True
        return False

    def apply_preparations(self) -> None:
        attributes_to_update = {
            "protection": 0,
            "power": 0,
            "hp": 0
        }

        if self.armour is not None:
            for item in self.armour:
                attributes_to_update["protection"] += item["protection"]

        attributes_to_update["power"] += self.weapon["power"]

        if self.potion is not None:
            potion_effect = self.potion["effect"]
            for attribute, value in potion_effect.items():
                if attribute in attributes_to_update:
                    attributes_to_update[attribute] += value

        for attribute, value in attributes_to_update.items():
            setattr(self, attribute, getattr(self, attribute) + value)
