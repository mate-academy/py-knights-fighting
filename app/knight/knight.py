class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.base_power = data["power"]
        self.hp = data["hp"]
        self.armour = data["armour"]
        self.weapon = data["weapon"]
        self.potion = data["potion"]

        self.power = self.base_power
        self.protection = 0

        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        self.protection = sum(
            piece["protection"] for piece in self.armour
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

    def take_damage(self, damage: int) -> None:
        self.hp = max(self.hp - damage, 0)
