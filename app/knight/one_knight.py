class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: dict | None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def one_knight_create(one_knight_dict: dict) -> "Knight":
        for key, value in one_knight_dict.items():
            knight = Knight(
                name=value["name"],
                power=value["power"],
                hp=value["hp"],
                armour=value["armour"],
                weapon=value["weapon"],
                potion=value["potion"],
            )
            return knight
