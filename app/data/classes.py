class Knight:

    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.protection = 0

        self.apply_armour(knight_data["armour"])
        self.apply_weapon(knight_data["weapon"])
        self.apply_potion(knight_data["potion"])

    def apply_armour(self, armour_list: list) -> None:
        for item in armour_list:
            self.protection += item["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            effect = potion["effect"]
            if "hp" in effect:
                self.hp += effect["hp"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        if damage > 0:
            self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
