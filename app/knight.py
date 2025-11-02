class Knight:

    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = 0

        self.prepare_for_duel()

    def prepare_for_duel(self) -> None:
        self.protection = sum(armour["protection"] for armour in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            for stat, value in self.potion["effect"].items():
                if hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) + value)

        self.hp = max(self.hp, 0)
        self.power = max(self.power, 0)
        self.protection = max(self.protection, 0)

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        if damage > 0:
            self.hp = max(0, self.hp - damage)

    def is_alive(self) -> bool:
        return self.hp > 0

    def __repr__(self) -> str:
        return (
            f"->Knight {self.name}: "
            f"HP = {self.hp}, "
            f"Power = {self.power}, "
            f"Protection = {self.protection}<-"
        )
