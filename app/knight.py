class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.power: int = config["power"]
        self.hp: int = config["hp"]
        self.armour: list[dict] = config["armour"]
        self.weapon: dict = config["weapon"]
        self.potion: dict | None = config["potion"]
        self.protection: int = 0

    def prepare(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def fight(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp <= 0:
            self.hp = 0
        if opponent.hp <= 0:
            opponent.hp = 0
