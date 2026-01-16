class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        print(f"\n{self.name} is coming on rumble!")
        self.show_stats()

    def take_damage(self, damage: int) -> None:
        damage = damage - self.protection if damage > self.protection else 0
        self.hp -= damage
        print(f"{self.name} receives {damage} points of damage.")

        if self.hp < 0:
            self.hp = 0
            print(f"Sir {self.name} is defeated. What a shame!")

    def show_stats(self) -> None:
        print(f"Sir {self.name} has {self.hp} HP."
              f"Battle skills - {self.power} might, {self.protection} armor")

    @classmethod
    def from_dict(cls, data: dict) -> "Knight":
        return cls(data["name"], data["power"], data["hp"])
