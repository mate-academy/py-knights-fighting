class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            protection: int,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def print_stats(self) -> None:
        print("------------------------------------------")
        print(f"Name: {self.name}\nHP: {self.hp}")
        print(f"Power: {self.power}\nProtection: {self.protection}")
        print("------------------------------------------")
