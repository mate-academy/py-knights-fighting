class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]

        self.hp = knight_data["hp"]

        self.power = (
            knight_data["power"]
            + knight_data["weapon"]["power"]
        )

        self.protection = sum(
            armour["protection"]
            for armour in knight_data["armour"]
        )

        potion = knight_data["potion"]

        if potion:
            effects = potion["effect"]

            self.hp += effects.get("hp", 0)

            self.power += effects.get("power", 0)

            self.protection += effects.get(
                "protection",
                0
            )

    def take_damage(self, damage: int) -> None:
        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
