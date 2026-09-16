class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict | None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

        self._apply_armour(armour)
        self._apply_weapon(weapon)
        self._apply_potion(potion)

    def _apply_armour(self, armour: list) -> None:
        self.protection = sum(piece["protection"] for piece in armour)

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return

        effect = potion["effect"]
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def take_damage(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection
        if self.hp <= 0:
            self.hp = 0

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )
