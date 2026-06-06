class Knights:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: dict,
        armour: list,
        potion: dict
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp

        self.weapon = weapon
        self.armour = armour
        self.potion = potion

        self.hp = hp
        self.power = power
        self.protection = 0

        self.apply_weapon()
        self.apply_armour()
        self.use_potion()

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_armour(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def use_potion(self) -> None:
        if self.potion is None:
            return

        effect = self.potion["effect"]

        if "hp" in effect:
            self.hp += effect["hp"]

        if "power" in effect:
            self.power += effect["power"]

        if "protection" in effect:
            self.protection += effect["protection"]

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection

        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0
