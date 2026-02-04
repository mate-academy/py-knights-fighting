class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

    def prepare(self) -> None:
        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        self.protection = sum(
            part["protection"] for part in self.armour
        )

    def _apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def _apply_potion(self) -> None:
        if not self.potion:
            return

        for stat, value in self.potion["effect"].items():
            if stat == "hp":
                self.hp += value
            elif stat == "power":
                self.power += value
            elif stat == "protection":
                self.protection += value

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0
