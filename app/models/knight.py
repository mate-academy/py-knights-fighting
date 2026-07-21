class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]

        self.protection = sum(
            armour["protection"]
            for armour in data["armour"]
        )

        self.power += data["weapon"]["power"]

        potion = data["potion"]
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def attack(self, enemy: "Knight") -> None:
        damage = self.power - enemy.protection
        enemy.hp = max(0, enemy.hp - damage)
