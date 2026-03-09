from app.models.equipment import Equipment, Potion


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]

        self.weapon = Equipment(
            config["weapon"]["name"],
            power=config["weapon"]["power"]
        )
        self.armour = [
            Equipment(part["part"], prot=part["protection"])
            for part in config["armour"]
        ]
        self.potion = None
        if config["potion"]:
            self.potion = Potion(
                config["potion"]["name"],
                config["potion"]["effect"]
            )

        self.hp = 0
        self.power = 0
        self.protection = 0
        self._prepare_for_battle()

    def _prepare_for_battle(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = sum(part.protection for part in self.armour)

        self.power += self.weapon.power

        if self.potion:
            self.hp += self.potion.hp
            self.power += self.potion.power
            self.protection += self.potion.protection

    def receive_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp = max(0, self.hp - damage)
