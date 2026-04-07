class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = sum(
            a["protection"] for a in config.get("armour", [])
        )

        self.power += config["weapon"]["power"]

        potion = config.get("potion")
        if potion:
            effects = potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = max(0, opponent_power - self.protection)
        self.hp = max(0, self.hp - damage)

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def __repr__(self) -> str:
        return (
            f"Knight({self.name!r}, hp={self.hp}, "
            f"power={self.power}, protection={self.protection})"
        )
