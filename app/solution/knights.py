class Knight:
    def __init__(
            self, name: str,
            hp: int,
            power: int,
            armour: list,
            weapon: dict,
            potion: dict | None) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def from_dict(cls, config: dict) -> "Knight":
        return cls(
            name=config["name"],
            hp=config["hp"],
            power=config["power"],
            armour=config.get("armour", []),
            weapon=config.get("weapon", {}),
            potion=config.get("potion"),
        )

    def prepare_stats(self) -> "Knight":
        # Armour
        self.protection = sum(a.get("protection", 0) for a in self.armour)
        # Weapon
        self.power += self.weapon.get("power", 0)
        # Potion
        if self.potion:
            eff = self.potion.get("effect", {})
            self.hp += eff.get("hp", 0)
            self.power += eff.get("power", 0)
            self.protection += eff.get("protection", 0)
        return self
