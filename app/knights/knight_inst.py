class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list[dict],
                 weapon: dict, potion: dict) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour_config = armour
        self.weapon_config = weapon
        self.potion_config = potion

        self.current_hp = hp
        self.current_power = power
        self.current_protection = 0

    def prepare_for_battle(self) -> None:
        for i in self.armour_config:
            self.current_protection += i["protection"]
        self.current_power = self.base_power + self.weapon_config["power"]
        if self.potion_config is not None:
            if "power" in self.potion_config["effect"]:
                self.current_power += self.potion_config["effect"]["power"]

            if "protection" in self.potion_config["effect"]:
                self.current_protection +=\
                    self.potion_config["effect"]["protection"]

            if "hp" in self.potion_config["effect"]:
                self.current_hp += self.potion_config["effect"]["hp"]

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.current_protection
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0

    def reset_stats(self) -> None:
        self.current_hp = self.base_hp
        self.current_power = self.base_power
        self.current_protection = 0
