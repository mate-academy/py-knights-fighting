class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]

        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        effects = self.potion["effect"]

        if "hp" in effects:
            self.hp += effects["hp"]

        if "power" in effects:
            self.power += effects["power"]

        if "protection" in effects:
            self.protection += effects["protection"]

    def fight(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection

        if self.hp <= 0:
            self.hp = 0