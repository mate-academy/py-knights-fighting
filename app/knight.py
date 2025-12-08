class Knight:

    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon")
        self.potion = config.get("potion")
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        if self.weapon is not None:
            self.power += self.weapon["power"]
        else:
            raise ValueError("Knight must have weapon")

    def apply_potion(self) -> None:
        if self.potion is None:
            return
        effect = self.potion.get("effect")
        if not isinstance(effect, dict):
            return
        if "power" in effect:
            self.power += effect["power"]

        if "protection" in effect:
            self.protection += effect["protection"]

        if "hp" in effect:
            self.hp += effect["hp"]
