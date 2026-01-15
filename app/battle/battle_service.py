from app.knights_person.knight import Knight


class Battle:
    @staticmethod
    def fight(first: Knight, second: Knight) -> None:
        first.hp -= second.power - first.protection
        second.hp -= first.power - second.protection

        if first.hp < 0:
            first.hp = 0

        if second.hp < 0:
            second.hp = 0

    @staticmethod
    def results(knights: dict[Knight]) -> dict:
        return {knight.name: knight.hp for knight in knights.values()}
