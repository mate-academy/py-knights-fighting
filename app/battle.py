from .knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def check_hp(self, knight: Knight) -> int:
        return 0 if knight.hp <= 0 else knight.hp

    def prepare_for_fight(self) -> None:
        self.first_knight.apply_armour()
        self.second_knight.apply_armour()

        self.first_knight.apply_weapon()
        self.second_knight.apply_weapon()

        self.first_knight.apply_potion()
        self.second_knight.apply_potion()

    def fight(self) -> dict[str, int]:
        self.first_knight.hp -= (
            self.second_knight.power - self.first_knight.protection
        )
        self.second_knight.hp -= (
            self.first_knight.power - self.second_knight.protection
        )

        first_knight_hp = self.check_hp(self.first_knight)
        second_knight_hp = self.check_hp(self.second_knight)

        return {
            self.first_knight.name: first_knight_hp,
            self.second_knight.name: second_knight_hp,
        }
