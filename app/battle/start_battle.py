from app.knights.create_knight import CreateKnight


class Battle:
    def __init__(self, knights_info: dict) -> None:
        self.knights = []
        for knight in knights_info.keys():
            self.knights.append(CreateKnight(knights_info[knight]))

    def preparations(self) -> None:
        for knight in self.knights:
            knight.prepare_for_battle()

    def hp_update(self) -> None:
        for knight in self.knights:
            knight.update_hp()

    @staticmethod
    def fight(knight1: CreateKnight, knight2: CreateKnight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

    def result_of_battle(self) -> dict:
        self.preparations()
        self.fight(self.knights[0], self.knights[2])
        self.fight(self.knights[1], self.knights[3])
        self.hp_update()
        return {
            knight.name: knight.hp for knight in self.knights
        }
