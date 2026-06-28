class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        for armour in config["armour"]:
            self.protection += armour["protection"]

        self.power += config["weapon"]["power"]

        if config["potion"]:
            for stat, value in config["potion"]["effect"].items():
                if stat == "hp":
                    self.hp += value
                elif stat == "power":
                    self.power += value
                elif stat == "protection":
                    self.protection += value

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
