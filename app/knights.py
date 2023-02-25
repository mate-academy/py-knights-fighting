class CreateKnights:
    def __init__(self,
                 name: str,
                 power: int,
                 protection: int,
                 hp: int,
                 ) -> None:
        self.name = name
        self.power = power
        self.protection = protection
        self.hp = hp

    @staticmethod
    def sub(knights_one, knights_two) -> int:
        if knights_one.protection < knights_two.power:
            knights_one.hp -= knights_two.power - knights_one.protection
            if knights_one.hp <= 0:
                return 0
            else:
                return knights_one.hp
        if knights_two.protection > knights_one.power:
            knights_two.hp -= knights_one.power - knights_two.protection
            if knights_two.hp <= 0:
                return 0
            else:
                return knights_two.hp
