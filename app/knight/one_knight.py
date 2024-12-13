class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list[dict], weapon: dict, potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def one_knight_create(one_knight_dict: dict) -> "Knight":
        for k, v in one_knight_dict.items():
            knight = Knight(
                name=v["name"],
                power=v["power"],
                hp=v["hp"],
                armour=v["armour"],
                weapon=v["weapon"],
                potion=v["potion"]
            )
            return knight
