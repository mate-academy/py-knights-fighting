class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: dict | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        if self.armour:
            self.protection += sum(
                part["protection"] for part in self.armour
            )

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
