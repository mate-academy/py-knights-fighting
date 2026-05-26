class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]

        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]

        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(
            item["protection"]
            for item in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        effects = self.potion["effect"]

        self.hp += effects.get("hp", 0)
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0
