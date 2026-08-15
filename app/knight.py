class Knight:

    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.armour = knight_config["armour"]
        self.weapon = knight_config["weapon"]
        self.potion = knight_config["potion"]
        self.protection = 0

        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.power += self.weapon["power"]
        for part in self.armour:
            self.protection += part["protection"]

        if self.potion is not None:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        actual_damage = max(0, damage - self.protection)
        self.hp = max(0, self.hp - actual_damage)
