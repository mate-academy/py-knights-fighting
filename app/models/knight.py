class Knight:  # Make sure this is a capital K!
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]

        self.hp: int = config.get("hp", 0)
        self.power: int = config.get("power", 0)
        self.protection: int = 0

        self._apply_armour(config.get("armour") or [])
        self._apply_weapon(config.get("weapon") or {})
        self._apply_potion(config.get("potion") or {})

    def _apply_armour(self, armour: list) -> None:
        self.protection += sum(part.get("protection", 0) for part in armour)

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power", 0)

    def _apply_potion(self, potion: dict) -> None:
        effect = potion.get("effect", {})
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
