class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0
        self._armour = config.get("armour", [])
        self._weapon = config["weapon"]
        potion = config.get("potion")
        self._potion = potion if potion is not None else None

    def prepare(self) -> None:
        for item in self._armour:
            self.protection += item.get("protection", 0)
        self.power += self._weapon.get("power", 0)
        potion = self._potion
        if potion is not None:
            effect = potion.get("effect", {})  # type: ignore
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
