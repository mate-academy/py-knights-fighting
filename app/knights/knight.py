class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armor(self) -> None:
        self.protection = sum([a.protection for a in self.armour])

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            effects = self.potion.effect
            if "power" in effects:
                self.power += effects["power"]
            if "protection" in effects:
                self.protection += effects["protection"]
            if "hp" in effects:
                self.hp += effects["hp"]

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def prepare_for_battle(self) -> None:
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()
