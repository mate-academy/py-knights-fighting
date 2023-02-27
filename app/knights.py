class CreateKnights:
    def __init__(self,
                 name: str,
                 power: int,
                 protection: int,
                 hp: int,
                 ) -> None:
        self.name: str = name
        self.power: int = power
        self.protection: int = protection
        self.hp: int = hp

    @staticmethod
    def fight(knights_one: object, knights_two: object) -> None:
        if knights_one.protection < knights_two.power:
            knights_one.hp -= knights_two.power - knights_one.protection
            if knights_one.hp <= 0:
                knights_one.hp = 0

        if knights_two.protection > knights_one.power:
            knights_two.hp -= knights_one.power - knights_two.protection
            if knights_two.hp <= 0:
                knights_two.hp = 0
