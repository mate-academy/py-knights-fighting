class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: str,
            weapon: str,
            potion: str
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_equipment(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        self.power += self.weapon.power
        if self.potion:
            self.potion.apply(self)

    def receive_damage(self, damage: int) -> None:
        effective_damage = max(0, damage - self.protection)
        self.hp -= effective_damage
        self.hp = max(0, self.hp)

    def is_alive(self) -> None:
        return self.hp > 0

    def __repr__(self) -> None:
        return (f"{self.name}(HP: {self.hp}, "
                f"Power: {self.power}, "
                f"Protection: {self.protection})")
