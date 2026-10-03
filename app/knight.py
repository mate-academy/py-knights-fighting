class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(
            armour_part["protection"]
            for armour_part in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        effects = self.potion["effect"]

        self.power += effects.get("power", 0)
        self.hp += effects.get("hp", 0)
        self.protection += effects.get("protection", 0)

    def fight(self, opponent: "Knight") -> None:
        damage_to_self = opponent.power - self.protection
        damage_to_opponent = self.power - opponent.protection

        self.hp -= damage_to_self
        opponent.hp -= damage_to_opponent

        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)
