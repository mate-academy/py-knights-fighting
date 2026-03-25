class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        self._apply_armour(config["armour"])
        self._apply_weapon(config["weapon"])
        self._apply_potion(config["potion"])

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

    def fight(self, opponent: "Knight") -> None:
        damage_to_self = opponent.power - self.protection
        damage_to_opponent = self.power - opponent.protection
        self.hp -= damage_to_self
        opponent.hp -= damage_to_opponent
        if self.hp < 0:
            self.hp = 0
        if opponent.hp < 0:
            opponent.hp = 0
