from app.knights_person.knight import Knight


class Battle:
    @staticmethod
    def fight(first: Knight, second: Knight) -> Knight:
        first.hp -= second.power - first.protection

        if first.hp <= 0:
            first.hp = 0
        return first

    @staticmethod
    def results(knights: list) -> dict:
        results = {}
        for knight in knights:
            results[knight.name] = knight.hp

        return results
