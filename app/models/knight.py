class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.protection = 0

        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            effects = self.potion["effect"]

            for characteristic, value in effects.items():
                current_value = getattr(self, characteristic)
                setattr(
                    self,
                    characteristic,
                    current_value + value,
                )

    def take_damage(self, enemy_power: int) -> None:
        self.hp -= enemy_power - self.protection

        if self.hp <= 0:
            self.hp = 0
