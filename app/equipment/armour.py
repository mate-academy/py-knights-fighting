class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    @staticmethod
    def from_list(armour: list) -> list:
        if armour:
            return [Armour(item["part"], item["protection"])
                    for item in armour]
