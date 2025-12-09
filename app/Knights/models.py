class Knight:
    def __init__(
            self,
            name: str,
            base_power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.power = 0
        self.protection = 0

        self.prepare_for_battle()

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        return cls(
            name=config["name"],
            base_power=config["power"],
            hp=config["hp"],
            armour=config.get("armour", []),
            weapon=config.get("weapon"),
            potion=config.get("potion"),
        )

    def prepare_for_battle(self) -> None:
        self._calculate_protection()
        self._apply_weapon()
        self._apply_potion()

    def _calculate_protection(self) -> None:
        protection = 0
        for piece in self.armour:
            protection += piece.get("protection", 0)
        self.protection = protection

    def _apply_weapon(self) -> None:
        power = self.base_power
        if self.weapon is not None:
            power += self.weapon.get("power", 0)
        self.power = power

    def _apply_potion(self) -> None:
        if self.potion is None:
            return

        effect = self.potion.get("effect", {})

        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)
