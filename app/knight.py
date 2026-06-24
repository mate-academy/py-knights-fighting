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
        self.power = power
        self.hp = hp
        self.protection = 0

        self._apply_armour(armour)
        self._apply_weapon(weapon)
        self._apply_potion(potion)

    def _apply_armour(self, armour: list) -> None:
        for piece in armour:
            self.protection += piece["protection"]

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return

        effect = potion["effect"]
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def receive_damage(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection
        if self.hp <= 0:
            self.hp = 0

    @classmethod
    def from_dict(cls, data: dict) -> "Knight":
        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data["potion"],
        )
