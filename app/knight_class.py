from __future__ import annotations


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data.get("name")
        self.power = self.calculate_character(knight_data, "power")
        self.hp = self.calculate_character(knight_data, "hp")
        self.protection = self.calculate_character(knight_data, "protection")

    def calculate_character(
            self,
            knight_data: dict | list,
            character: str
    ) -> int:
        result_value = 0

        for character_name, character_value in knight_data.items():
            if isinstance(character_value, dict):
                result_value += self.calculate_character(character_value,
                                                         character)
            if isinstance(character_value, list):
                for element in character_value:
                    result_value += self.calculate_character(element,
                                                             character)
            elif character_name == character:
                result_value += character_value

        return result_value

    def fight(self, knight_x: Knight) -> None:
        self.hp -= knight_x.power - self.protection
        self.check_defeat()

    def check_defeat(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def check_hp(self) -> int:
        return self.hp
