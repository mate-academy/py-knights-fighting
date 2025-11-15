from app.knights.knights import Character


class Battle:
    def __init__(self, character_one: Character,
                 character_two: Character) -> None:
        self.character_one = character_one
        self.character_two = character_two

    def calculate_battle(self) -> None:
        self.character_one.hp -= (self.character_two.power
                                  - self.character_one.protection)
        self.character_two.hp -= (self.character_one.power
                                  - self.character_two.protection)

        if self.character_one.hp <= 0:
            self.character_one.hp = 0

        if self.character_two.hp <= 0:
            self.character_two.hp = 0
