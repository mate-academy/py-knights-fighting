from __future__ import annotations


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data.get("name")
        self.power = self.calculation_character(knight_data, "power")
        self.hp = self.calculation_character(knight_data, "hp")
        self.protection = self.calculation_character(knight_data, "protection")

    def calculation_character(
            self,
            knight_data: dict | list,
            character: str
    ) -> int:
        result_value = 0

        for character_name, character_value in knight_data.items():
            if isinstance(character_value, dict):
                result_value += self.calculation_character(character_value,
                                                           character)
            if isinstance(character_value, list):
                for elem in character_value:
                    result_value += self.calculation_character(elem, character)
            elif character_name == character:
                result_value += character_value

        return result_value

    def fight(self, knight_x: Knight) -> None:
        self.hp -= knight_x.power - self.protection
        self.check_def()

    def check_def(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def check_hp(self) -> int:
        return self.hp
