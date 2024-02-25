class Armor:
    def __init__(self, armor: list) -> None:
        self.armor_parts = armor

    def protection(self) -> int:
        total_protection = 0
        for armor_part in self.armor_parts:
            total_protection += armor_part["protection"]
        return total_protection
