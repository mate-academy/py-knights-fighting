class Knight:

    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.armour = knight_info["armour"]
        self.weapon = knight_info["weapon"]
        self.potion = knight_info["potion"]

    def calculate_stats(self) -> dict:
        stats = {"hp": self.hp,
                 "power": self.power + self.weapon["power"],
                 "protection": sum([add_prot["protection"]
                                    for add_prot in self.armour])}
        if self.potion:
            stats["hp"] += self.potion["effect"]["hp"]
            stats["power"] += self.potion["effect"]["power"]
            stats["protection"] += self.potion["effect"].get("protection", 0)
        return stats
