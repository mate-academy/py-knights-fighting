class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config.get("name")
        self.hp = config.get("hp", 0)
        self.power = config.get("power", 0)
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon", {})
        self.potion = config.get("potion")
        self.protection = config.get("protection", 0)

    def apply_armour(self) -> None:
        self.protection = (
            sum(armour_element.get("protection", 0)
                for armour_element in self.armour)
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if not self.potion:
            return
        for stat, delta in self.potion.get("effect", {}).items():
            setattr(self, stat, getattr(self, stat, 0) + delta)

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
