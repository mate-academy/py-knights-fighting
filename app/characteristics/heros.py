class Hero:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def __str__(self) -> str:
        return (f"Hero: {self.name}, power: {self.power}, "
                f"hp: {self.hp}, protection: {self.protection}")
