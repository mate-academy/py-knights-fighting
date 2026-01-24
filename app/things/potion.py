class Potion:
    def __init__(self,
                 name: str,
                 hp: int = 0,
                 power: int = 0,
                 protection: int = 0) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    @classmethod
    def create_potion_from_dict(cls,
                                dictionary: dict | None) -> Potion | None:
        if dictionary is None:
            return None
        potion = cls(name=dictionary["name"])
        character_stat = ["hp", "power", "protection"]
        for stat in character_stat:
            if stat in dictionary["effect"]:
                setattr(potion, stat, dictionary["effect"][stat])
        return potion
