class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.protection = 0

        self.apply_armour(knight_data["armour"])
        self.apply_weapon(knight_data["weapon"])
        self.apply_potion(knight_data["potion"])

    def apply_armour(self, armour: list) -> None:
        for armour_part in armour:
            self.protection += armour_part["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return

        for stat, value in potion["effect"].items():
            setattr(self, stat, getattr(self, stat) + value)

    def take_damage(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection

        if self.hp <= 0:
            self.hp = 0
