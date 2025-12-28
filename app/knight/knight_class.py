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

    def get_armour(self) -> None:
        self.protection += sum(part["protection"] for part in self.armour)

    def get_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def get_potion(self) -> None:
        if self.potion:
            effects = self.potion.get("effect", {})
            self.power += effects.get("power", 0)
            self.hp += effects.get("hp", 0)
            self.protection += effects.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.protection = 0
        self.get_armour()
        self.get_weapon()
        self.get_potion()
