class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion) -> None:
        # Statystyki bazowe (nigdy ich nie zmieniamy!)
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        # Statystyki bojowe (aktualizowane w prepare)
        self.current_power = power
        self.current_hp = hp
        self.protection = 0

    @classmethod
    def from_config(cls, config: dict):
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )

    def apply_protection(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self):
        self.current_power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effects = self.potion["effect"]

            self.current_power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.current_hp += effects.get("hp", 0)

    def prepare(self) -> None:
        self.current_power = self.base_power
        self.current_hp = self.base_hp
        self.protection = 0

        self.apply_protection()
        self.apply_weapon()
        self.apply_potion()

    def get_damage(self, attack_power: int) -> None:
        net_damage = max(0, attack_power - self.protection)
        self.hp = max(0, self.hp - net_damage)
