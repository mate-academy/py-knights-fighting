class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

        self.protection = 0

    def prepare_for_battle(self) -> "Knight":
        for arm_point in self.armour:
            self.protection += arm_point["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

        return self

    def attack(self, enemy: "Knight") -> None:
        damage = max(0, self.power - enemy.protection)
        enemy.hp -= damage

        if enemy.hp <= 0:
            enemy.hp = 0
