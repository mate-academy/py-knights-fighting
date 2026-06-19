from app.knight import Knight


class Championship:
    def __init__(self, knights: dict) -> None:
        self.knights = {
            "lancelot": Knight(knights["lancelot"]),
            "arthur": Knight(knights["arthur"]),
            "mordred": Knight(knights["mordred"]),
            "red_knight": Knight(knights["red_knight"]),
        }

    def prepare_knights(self) -> None:
        for knight in self.knights.values():
            knight.prepare_for_battle()

    def get_fight_pairs(self) -> list[tuple[Knight, Knight]]:
        return [
            (self.knights["lancelot"], self.knights["mordred"]),
            (self.knights["arthur"], self.knights["red_knight"]),
        ]

    @staticmethod
    def one_fight(first_knight: Knight, second_knight: Knight) -> None:
        second_knight.hp -= first_knight.power - second_knight.protection
        first_knight.hp -= second_knight.power - first_knight.protection
        if first_knight.hp <= 0:
            first_knight.hp = 0
        if second_knight.hp <= 0:
            second_knight.hp = 0

    def run_battles(self) -> None:
        for first_knight, second_knight in self.get_fight_pairs():
            self.one_fight(first_knight, second_knight)

    def get_results(self) -> dict:
        results = {
            knight.name: knight.hp
            for knight in self.knights.values()
        }
        return results
