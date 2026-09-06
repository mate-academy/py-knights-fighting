class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config["armour"]
        self.potion = config["potion"]
        self.protection = 0
        self.weapon = config["weapon"]

    def apply_armour(self) -> None:
        self.protection = sum(armour["protection"] for armour in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        for stat, value in self.potion["effect"].items():
            setattr(self, stat, getattr(self, stat) + value)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def fight(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        self.hp = max(self.hp, 0)
        opponent.hp = max(opponent.hp, 0)
