class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: (dict, None),
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def get_ready_to_battle(self) -> None:
        self.protection += sum(item.
                               get("protection", 0)
                               for item in self.armour)
        self.power += self.weapon.get("power", 0)

        if self.potion:
            buff = self.potion.get("effect", {})
            for attr in ["power", "hp", "protection"]:
                if attr in buff:
                    current_value = getattr(self, attr)
                    setattr(self, attr, current_value + buff[attr])

    @classmethod
    def battle_preparations(cls, knight_dict: dict) -> list:
        knights = [cls(**knight_dict[knight]) for knight in knight_dict]

        for knight in knights:
            knight.get_ready_to_battle()

        return knights

    @staticmethod
    def result(first: "Knight", second: "Knight") -> None:
        first.hp -= second.power - first.protection
        second.hp -= first.power - second.protection

        if first.hp < 0:
            first.hp = 0
        if second.hp < 0:
            second.hp = 0
