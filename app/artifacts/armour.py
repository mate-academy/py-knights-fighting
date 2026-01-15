from app.battle_field.stats import Stats


class Armour:
    def __init__(self) -> None:
        self.protection = 0
        self.parts = []

    def add_part(self, part: "ArmourPart") -> None:
        self.parts.append(part)

    def get_stats(self) -> Stats:
        res = Stats(0, 0, 0)
        for part in self.parts:
            res += part.get_stats()

        return res


class ArmourPart:
    def __init__(self, part_name: str, part_protection: int) -> None:
        self.name = part_name
        self.protection = part_protection

    def get_stats(self) -> Stats:
        return Stats(hp=0, power=0, protection=self.protection)
