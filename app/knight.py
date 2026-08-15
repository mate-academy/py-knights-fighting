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
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

        for part in self.armour:
            self.protection += part.get("protection", 0)

        if self.potion and "effect" in self.potion:
            effects = self.potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def take_damage(self, attacker_power: int) -> None:
        damage = attacker_power - self.protection
        if damage > 0:
            self.hp = max(0, self.hp - damage)
