from knight_description.knight import Knight


class Championship:
    knights = {}
    battle_results = {}

    @classmethod
    def init(cls) -> None:
        cls.knights = {}
        cls.battle_results = {}

    @classmethod
    def fill_out_knights(cls, knights: dict) -> None:
        for knight_sign, knight_stats in knights.items():
            new_knight = Knight.create_knight(knight_stats)
            cls.knights[knight_sign] = new_knight

    @classmethod
    def battle(cls, knight1_name: str, knight2_name: str) -> None:
        knight1 = cls.knights[knight1_name]
        knight2 = cls.knights[knight2_name]

        knight1.prepare_for_battle()
        knight2.prepare_for_battle()

        knight1.hp -= max(knight2.power - knight1.protection, 0)
        knight2.hp -= max(knight1.power - knight2.protection, 0)

        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0

        cls.battle_results[knight1.name] = knight1.hp
        cls.battle_results[knight2.name] = knight2.hp
