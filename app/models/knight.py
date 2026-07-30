class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self._apply_equipment()

    def _apply_equipment(self) -> None:
        # Armour
        for part in self.armour:
            self.protection += part.get("protection", 0)

        # Weapon
        if self.weapon:
            self.power += self.weapon.get("power", 0)

        # Potion
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def fight(self, opponent: "Knight") -> None:
        damage = max(0, opponent.power - self.protection)
        self.hp = max(0, self.hp - damage)
