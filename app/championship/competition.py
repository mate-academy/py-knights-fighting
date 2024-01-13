from app.participants.knight import Knight


class Competition:

    def fight(self, first_knight: Knight, second_knight: Knight) -> dict:
        first_knight.hp -= (second_knight.power - first_knight.protection)
        second_knight.hp -= (first_knight.power - second_knight.protection)

        self.check_hp([first_knight, second_knight])

        return {
            first_knight.name: first_knight.hp,
            second_knight.name: second_knight.hp
        }

    def check_hp(self, knights: list[Knight]) -> None:
        for knight in knights:
            if knight.hp < 0:
                knight.hp = 0
