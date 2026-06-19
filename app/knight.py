class Knight:
    def __init__(self, knights_data: dict) -> None:
        self.name = knights_data["name"]
        self.power = knights_data["power"]
        self.hp = knights_data["hp"]
        self.armour = knights_data["armour"]
        self.weapon = knights_data["weapon"]
        self.potion = knights_data["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            for attribute, bonus in self.potion["effect"].items():
                current_value = getattr(self, attribute)
                setattr(self, attribute, current_value + bonus)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
