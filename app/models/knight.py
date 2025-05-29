class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.armour = knight_data["armour"]
        self.protection = 0
        self.weapon = knight_data["weapon"]
        self.weapon_applied = False
        self.potion = knight_data["potion"]
        self.potion_applied = False

    def calculate_protection(self) -> None:
        self.protection = sum(item["protection"] for item in self.armour)

    def add_power(self) -> None:
        if not self.weapon_applied:
            self.power += self.weapon["power"]
            self.weapon_applied = True

    def add_potion(self) -> None:
        if self.potion and not self.potion_applied:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)
            self.potion_applied = True
