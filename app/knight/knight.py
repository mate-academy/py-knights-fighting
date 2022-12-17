class Knight:

    def __init__(
            self, knight_stats: dict
    ) -> None:
        self.name = knight_stats["name"]
        self.power = knight_stats["power"]
        self.hp = knight_stats["hp"]
        self.armour = knight_stats["armour"]
        self.weapon = knight_stats["weapon"]
        self.potion = knight_stats["potion"]

    def check_hp_after_battle(self) -> None:
        if self.hp < 0:
            self.hp = 0
