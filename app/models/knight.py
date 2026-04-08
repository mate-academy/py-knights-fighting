class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.hp: int = config["hp"]
        self.base_power: int = config["power"]
        self.protection: int = sum(
            item["protection"] for item in config["armour"]
        )
        self.weapon_power: int = config["weapon"]["power"]
        self.potion: dict | None = config["potion"]

        self._apply_equipment()

    def _apply_equipment(self) -> None:
        self.power: int = self.base_power + self.weapon_power

        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        if damage > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    @staticmethod
    def fight(knight_1: "Knight", knight_2: "Knight") -> None:
        k1_attack = knight_1.power
        k2_attack = knight_2.power

        knight_1.take_damage(k2_attack)
        knight_2.take_damage(k1_attack)
