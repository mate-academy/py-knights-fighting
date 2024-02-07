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
        if self.armour is not None:
            for item in self.armour:
                self.protection += item["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            potion_effect = self.potion["effect"]
            self.power += potion_effect.get("power", 0)
            self.protection += potion_effect.get("protection", 0)
            self.hp += potion_effect.get("hp", 0)
