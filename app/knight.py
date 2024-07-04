class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list = None,
            weapon: dict = None,
            potion: dict = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour if armour is not None else []
        self.weapon = weapon
        self.potion = potion
        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for piece in self.armour:
            self.protection += piece.get("protection", 0)

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage - self.protection)
        if self.hp < 0:
            self.hp = 0

    def __repr__(self) -> str:
        return (f"{self.name}: "
                f"{self.hp} HP, "
                f"{self.power} Power, "
                f"{self.protection} Protection")
