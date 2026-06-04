class KnightConfig:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

        self.protection = 0
        self.init_protection()
        self.init_power()
        self.init_potion()

    def init_protection(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def init_power(self) -> None:
        self.power += self.weapon["power"]

    def init_potion(self) -> None:
        if not self.potion:
            return

        effects = self.potion.get("effect", {})
        for stat_name, stat_value in effects.items():
            current_value = getattr(self, stat_name)

            new_value = current_value + stat_value
            setattr(self, stat_name, new_value)
