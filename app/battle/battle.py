from app.character.knight_konfiguration import Character


class Battle:
    result = {}

    def __init__(self,
                 first_knight: Character,
                 second_knight: Character
                 ) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def battle_of_knights(self) -> dict:
        self.first_knight.hp -= (
            self.second_knight.power - self.first_knight.protection)
        self.second_knight.hp -= (
            self.first_knight.power - self.second_knight.protection)

        if self.first_knight.hp <= 0:
            self.first_knight.hp = 0

        if self.second_knight.hp <= 0:
            self.second_knight.hp = 0

        Battle.result[self.first_knight.name] = self.first_knight.hp
        Battle.result[self.second_knight.name] = self.second_knight.hp

        return Battle.result
