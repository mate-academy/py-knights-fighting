from app.items.item import Item


class Potion(Item):
    def __init__(self, name: str,
                 hp: int = 0,
                 power: int = 0, protection: int = 0) -> None:
        super().__init__(name)
        self.hp = hp
        self.power = power
        self.protection = protection

    @staticmethod
    def create_potion(config: dict) -> "Potion":
        return Potion(name=config["name"],
                      hp=config["effect"].get("hp", 0),
                      power=config["effect"].get("power", 0),
                      protection=config["effect"].get("protection", 0))
