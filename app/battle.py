from app.knight import Knight


class Battle:
    battle_result = {}

    def __init__(
            self,
            first_knight: Knight,
            second_knight: Knight
    ) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def battle_round(self) -> None:
        first_knight_hp = (self.first_knight.hp - (
            self.second_knight.power - self.first_knight.protection
        ))
        second_knight_hp = (self.second_knight.hp - (
            self.first_knight.power - self.second_knight.protection
        ))

        if first_knight_hp <= 0:
            first_knight_hp = 0
        else:
            self.first_knight.update_hp(first_knight_hp)

        if second_knight_hp <= 0:
            second_knight_hp = 0
        else:
            self.second_knight.update_hp(second_knight_hp)

        Battle.battle_result.update({
            self.first_knight.name: first_knight_hp,
            self.second_knight.name: second_knight_hp
        })

    def __str__(self) -> str:
        return str(Battle.battle_result)
