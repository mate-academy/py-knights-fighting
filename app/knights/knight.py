class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: None | dict,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion.get("effect", {})

            for attribute, value in effect.items():
                if hasattr(self, attribute):
                    current_value = getattr(self, attribute)
                    setattr(self, attribute, current_value + value)
