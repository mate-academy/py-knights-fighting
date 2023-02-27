class Knights:
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

    def fight(self, knights_two: "Knights") -> None:
        if self.protection < knights_two.power:
            self.hp -= knights_two.power - self.protection
            if self.hp <= 0:
                self.hp = 0

        if knights_two.protection > self.power:
            knights_two.hp -= self.power - knights_two.protection
            if knights_two.hp <= 0:
                knights_two.hp = 0
