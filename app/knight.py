class Knight:
    def __init__(self, name: str, power: int, hp: int):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    @classmethod
    def create_knight_from_dict(cls, knight_dict: dict):
        return cls(
            knight_dict["name"],
            knight_dict["power"],
            knight_dict["hp"]
        )

    @classmethod
    def create_and_prepare_knight(cls, knight_dict: dict):
        knight = cls.create_knight_from_dict(knight_dict)
        knight.apply_weapon(knight_dict["weapon"])
        knight.apply_armour(knight_dict["armour"])
        knight.apply_potion_if_exist(knight_dict["potion"])
        return knight

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_armour(self, armour: list[dict]) -> None:
        for item in armour:
            self.protection += item["protection"]

    def apply_potion_if_exist(self, potion: dict) -> None:
        if potion is None:
            return

        effect = potion["effect"]
        for stat in ("protection", "power", "hp"):
            if stat not in effect:
                effect[stat] = 0

        self.hp += effect["hp"]
        self.power += effect["power"]
        self.protection += effect["protection"]

    @staticmethod
    def get_all_knights_hp(knights: list) -> dict:
        return {
            knight.name: knight.hp for knight in knights
        }
