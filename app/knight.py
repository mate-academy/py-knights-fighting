class Knight:
    def __init__(self,
                 config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = 0

        self.apply_armour(self.armour)
        self.apply_weapon(self.weapon)
        self.apply_potion(self.potion)

    def apply_armour(self, armour: list) -> None:
        for piece in armour:
            self.protection += piece["protection"]

    def apply_weapon(self, weapon: list) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion is None:
            return

        effect = potion["effect"]

        if "hp" in effect:
            self.hp += effect["hp"]
        if "power" in effect:
            self.power += effect["power"]
        if "protection" in effect:
            self.protection += effect["protection"]

    def take_damage(self, opponent_power: int) -> None:
        damage = max(0, opponent_power - self.protection)
        self.hp = max(0, self.hp - damage)

    def is_alive(self) -> bool:
        return self.hp > 0
