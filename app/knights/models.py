class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.protection = 0

        self._apply_armour(config["armour"])
        self._apply_weapon(config["weapon"])
        self._apply_potion(config["potion"])

    def _apply_armour(self, armour_list: list) -> None:
        for item in armour_list:
            self.protection += item["protection"]

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: dict) -> None:
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
