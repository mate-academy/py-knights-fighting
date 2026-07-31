from app.knight import Knight


class Battle:
    @staticmethod
    def prepare(knight: Knight) -> None:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    @staticmethod
    def fight(first: Knight, second: Knight) -> None:
        first.hp -= second.power - first.protection
        second.hp -= first.power - second.protection

        first.hp = max(first.hp, 0)
        second.hp = max(second.hp, 0)
