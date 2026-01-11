class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]

        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

        self.protection = 0
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        # armour
        self.protection = sum(a["protection"] for a in self.armour)

        if self.protection < 0:
            self.protection = 0

        # weapon
        self.power += self.weapon["power"]

        # potion
        if self.potion is not None:
            effect = self.potion["effect"]

            if "power" in effect:
                self.power += effect["power"]

            if "protection" in effect:
                self.protection += effect["protection"]

            if "hp" in effect:
                self.hp += effect["hp"]

    def take_hit(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        if damage < 0:
            damage = 0

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0
