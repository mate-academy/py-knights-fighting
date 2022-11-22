from app.units.knight import Knight


class Battle:
    def __init__(self, lancelot: Knight, arthur: Knight,
                 mordred: Knight, red_knight: Knight) -> None:
        self.lancelot = lancelot
        self.arthur = arthur
        self.mordred = mordred
        self.red_knight = red_knight

        self.prepare([self.lancelot,
                      self.arthur,
                      self.mordred,
                      self.red_knight])

    @staticmethod
    def prepare(knights: list) -> None:
        for knight in knights:
            knight.prepare_to_battle()

    def execute(self) -> dict:
        # 1 Lancelot vs Mordred
        self.lancelot.hp -= self.mordred.power - self.lancelot.protection
        self.mordred.hp -= self.lancelot.power - self.mordred.protection
        if self.lancelot.hp <= 0:
            self.lancelot.hp = 0
        if self.mordred.hp <= 0:
            self.mordred.hp = 0

        # 2 Arthur vs Red Knight
        self.arthur.hp -= self.red_knight.power - self.arthur.protection
        self.red_knight.hp -= self.arthur.power - self.red_knight.protection
        if self.arthur.hp <= 0:
            self.arthur.hp = 0
        if self.red_knight.hp <= 0:
            self.red_knight.hp = 0
        return {
            self.lancelot.name: self.lancelot.hp,
            self.arthur.name: self.arthur.hp,
            self.mordred.name: self.mordred.hp,
            self.red_knight.name: self.red_knight.hp
        }
