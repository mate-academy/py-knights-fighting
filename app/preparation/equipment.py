class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return f"{self.part}, {self.protection}"


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> str:
        return f"{self.name}, {self.power}"


class Potion:
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self.power = 0
        self.hp = 0
        self.protection = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        attrs = ["power", "hp", "protection"]
        existing_attrs = [
            f"{attr}: {getattr(self, attr)}"
            for attr in attrs if hasattr(self, attr)
        ]
        effects = ", ".join(existing_attrs)
        return f"Potion: {self.name}, {effects}"
