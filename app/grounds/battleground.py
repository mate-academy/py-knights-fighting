from app.people.knights import Knight


class Battleground:
    def __init__(self, bg_number: int) -> None:
        self.bg_number = bg_number

    def bg_battle(self, knight1: Knight, knight2: Knight) -> None:
        if all([knight1.equipment_applied, knight2.equipment_applied]):
            knight1.hp -= knight2.power - knight1.protection
            knight2.hp -= knight1.power - knight2.protection
            if knight1.hp <= 0:
                knight1.hp = 0
            if knight2.hp <= 0:
                knight2.hp = 0
