from app.contest import preparations


class Contest:
    def __init__(self, knights: dict):
        self.knights = knights
        self.battle_results = {}

    def make_all_contest_preparations(self):
        for knight in self.knights.values():
            preparations.apply_armor(knight)
            preparations.apply_weapon(knight)
            preparations.apply_potion(knight)

    def make_battle(self, first_knight_name: str, second_knight_name: str) -> None:
        first_knight = self.knights.get(first_knight_name)
        second_knight = self.knights.get(second_knight_name)
        first_knight.hp -= second_knight.power - first_knight.protection
        if first_knight.hp <= 0:
            first_knight.hp = 0
        self.battle_results.update({first_knight_name: first_knight.hp})

        second_knight.hp -= first_knight.power - second_knight.protection
        if second_knight.hp <= 0:
            second_knight.hp = 0
        self.battle_results.update({second_knight_name: second_knight.hp})

