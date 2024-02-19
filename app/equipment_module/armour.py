
class ArmourPart:

    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection


class Armour:

    def __init__(self, armour: list) -> None:
        self.armour_parts = []
        self.create_armour_set(armour)

    def create_armour_set(self, armour_set: dict) -> None:
        for armour_part in armour_set:
            armour_obj = ArmourPart(
                name=armour_part["part"],
                protection=armour_part["protection"]
            )
            self.armour_parts.append(armour_obj)
