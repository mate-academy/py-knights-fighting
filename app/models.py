class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon", None)
        self.potion = config.get("potion", None)
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if not self.potion:
            return
        effects = self.potion.get("effect", {})
        self.hp += effects.get("hp", 0)
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def receive_damage(self, attack_power) -> None:
        damage = max(attack_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)
