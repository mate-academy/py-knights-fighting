from app.pkg.knight import Knight


class Battle:

    @staticmethod
    def gear_check(knight: Knight) -> Knight:
        knight.apply_weapon(knight.weapon)
        knight.apply_armour(knight.armour)
        knight.apply_potion_effect(knight.potion)

        return knight

    @staticmethod
    def check_hp(hp: int) -> int:
        if hp < 0:
            return 0
        return hp

    @staticmethod
    def fight(knight_one: Knight, knight_two: Knight) -> tuple[Knight, Knight]:
        knight_one.hp -= knight_two.power - knight_one.protection
        knight_two.hp -= knight_one.power - knight_two.protection

        return knight_one, knight_two
