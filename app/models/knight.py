from app.utils.stats import Armour, Weapon, Potion


class Knight:
    """Knight character with stats and preparation logic."""

    name: str
    power: int | float
    hp: int | float
    armour: list[Armour]
    weapon: Weapon
    potion: Potion | None

    def __init__(
        self,
        *,
        name: str,
        power: int | float,
        hp: int | float,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion | None,
    ) -> None:
        """Initialize knight with stats."""
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def prepare(self) -> None:
        """Apply armour, weapon, and potion effects."""
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        """Sum protection from all armour pieces."""
        self.protection = 0
        for armour_piece in self.armour:
            self.protection += armour_piece["protection"]

    def apply_weapon(self) -> None:
        """Add weapon power to base power."""
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        """Apply potion effects to hp, power, and protection."""
        if self.potion is not None:
            for stat, value in self.potion["effect"].items():
                if stat == "power":
                    self.power += value
                elif stat == "protection":
                    self.protection += value
                elif stat == "hp":
                    self.hp += value
