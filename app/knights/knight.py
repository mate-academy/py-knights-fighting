class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, protection: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        knight = cls(config["name"],
                     config["power"],
                     config["hp"],
                     0)
        knight.protection += sum([armour_part["protection"]
                                  for armour_part in config["armour"]])
        knight.power += config["weapon"]["power"]
        if config["potion"] is not None:
            for stat, value in config["potion"]["effect"].items():
                setattr(knight, stat, getattr(knight, stat) + value)
        return knight

    def take_hit(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        if self.hp <= 0:
            self.hp = 0
