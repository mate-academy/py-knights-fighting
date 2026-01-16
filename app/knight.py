class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = self.apply_power(config)
        self.protection = self.apply_armour(config)
        self.hp = self.apply_hp(config)

    @staticmethod
    def apply_armour(config) -> int:
        protection = 0

        if config["potion"] is not None:
            if "protection" in config["potion"]["effect"]:
                protection += config["potion"]["effect"]["protection"]

        for a in config["armour"]:
            protection += a["protection"]
        return protection

    @staticmethod
    def apply_power(config) -> int:
        power = config["power"] + config["weapon"]["power"]

        if config["potion"] is not None:
            if "power" in config["potion"]["effect"]:
                power += config["potion"]["effect"]["power"]
        return power

    @staticmethod
    def apply_hp(config) -> int:
        hp = config["hp"]

        if config["potion"] is not None:
            if "hp" in config["potion"]["effect"]:
                hp += config["potion"]["effect"]["hp"]
        return hp

    def __repr__(self) -> str:
        return (f" name: {self.name}, "
                f"power: {self.power}, "
                f"protection: {self.protection}, "
                f"hp: {self.hp}")

    def duel_with(self, other) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
