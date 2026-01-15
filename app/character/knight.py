class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def knight_preparation(cls, knights: dict[dict]) -> list:
        result = []
        for one in knights:
            knight_dict = knights[one]
            # create knight
            knight = cls.create_knight(knight_dict)
            # apply weapon
            knight.apply_weapon(knight_dict["weapon"]["power"])
            # apply armour if exist
            knight.apply_armour(knight_dict["armour"])
            # apply potion if exist
            knight.apply_potion(knight_dict["potion"])

            result += [knight]
        return result

    @classmethod
    def create_knight(cls, knight_dict: dict) -> object:
        return cls(
            name=knight_dict["name"],
            power=knight_dict["power"],
            hp=knight_dict["hp"]
        )

    def apply_weapon(self, weapon_power: int) -> None:
        self.power += weapon_power

    def apply_armour(self, armour: dict) -> None:
        if armour is not None:
            for ar in armour:
                self.protection += ar["protection"]

    def apply_potion(self, potion: dict) -> None:
        if potion:
            potion_effect = potion["effect"]
            for attribute, effect in potion_effect.items():
                current_value = getattr(self, attribute, 0)
                setattr(self, attribute, current_value + effect)
