class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def drink(self) -> None:
        potion_effect = self.potion.get("effect")
        if potion_effect:
            self.hp += potion_effect.get("hp", 0)
            self.power += potion_effect.get("power", 0)
            self.protection += potion_effect.get("protection", 0)

    def preparation(self) -> None:
        self.power += self.weapon.get("power")

        if self.armour:
            self.protection += sum(
                arm.get("protection") for arm in self.armour
            )

        if self.potion:
            self.drink()

    def duel(self, other: "Knight") -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.hp = max(self.hp, 0)
        other.hp = max(other.hp, 0)
