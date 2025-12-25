class Knight:
    def __init__(
            self, name: str, power: int, hp: int, armour: list,
            weapon: dict, potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        total_protection: int = sum(part["protection"] for part in self.armour)
        self.protection: int = total_protection

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(damage - self.protection, 0)
        self.hp = max(0, self.hp)
