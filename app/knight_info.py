class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.protection = 0

        self.apply_armour(data["armour"])
        self.apply_weapon(data["weapon"])
        self.apply_potion(data["potion"])

    def apply_armour(self, armour: list) -> None:
        for armour_part in armour:
            self.protection += armour_part["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion is None:
            return

        for key, value in potion["effect"].items():
            if key == "power":
                self.power += value
            elif key == "hp":
                self.hp += value
            elif key == "protection":
                self.protection += value

    def damage(self, enemy_power: int) -> None:
        self.hp -= enemy_power - self.protection

        if self.hp <= 0:
            self.hp = 0
