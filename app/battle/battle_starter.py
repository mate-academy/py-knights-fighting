from app.knights.knight_creation import Knight


class Battle:
    def __init__(self, knights_config: dict) -> None:
        self.knights = [Knight(knights_config[name])
                        for name in knights_config.keys()]

    @staticmethod
    def fight(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection

    def prepare_all_knights(self) -> None:
        for knight in self.knights:
            knight.prepare_to_battle()

    def update_knights_hp(self) -> None:
        for knight in self.knights:
            knight.update_hp()
