class Knight:
    def __init__(self, knight_dict: dict) -> None:
        self.name = knight_dict["name"]
        self.power = knight_dict["power"]
        self.hp = knight_dict["hp"]
        self.armour = knight_dict.get("armour", [])
        self.weapon = knight_dict.get("weapon", {})
        self.potion = knight_dict.get("potion", {})
        self.protection = 0

        self.apply_weapon()
        self.apply_armour()
        self.apply_potion()

    def apply_potion(self) -> None:
        if self.potion:
            effects_list = self.potion["effect"]
            if "hp" in effects_list:
                self.hp += effects_list["hp"]
            if "power" in effects_list:
                self.power += effects_list["power"]
            if "protection" in effects_list:
                self.protection += effects_list["protection"]

    def apply_armour(self) -> None:
        for armour in self.armour:
            if "protection" in armour:
                self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon["power"]

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection

        if damage > 0:
            self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
