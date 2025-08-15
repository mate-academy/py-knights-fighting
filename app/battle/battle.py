from app.knight.lancelot import Lancelot
from app.knight.mordred import Mordred
from app.knight.arthur import Arthur
from app.knight.redknight import RedKnight
from app.knight.knights import Knight


class BattleSimulator:

    def __init__(self, lancelot: dict, arthur: dict, mordred: dict,
                 red_knight: dict) -> None:
        self.lancelot = lancelot
        self.mordred = mordred
        self.arthur = arthur
        self.red_knight = red_knight

    def conduct_one_on_one_battle(self, knight1: Knight,
                                  knight2: Knight) -> None:
        # Логіка самого бою
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        # Перевірка, чи не загинув хтось у бою
        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0

    def run_all_battles(self) -> None:
        # BATTLE 1: Lancelot vs Mordred
        self.conduct_one_on_one_battle(self.lancelot, self.mordred)

        # BATTLE 2: Arthur vs Red Knight
        self.conduct_one_on_one_battle(self.arthur, self.red_knight)

        return {
            self.lancelot.name: self.lancelot.hp,
            self.arthur.name: self.arthur.hp,
            self.mordred.name: self.mordred.hp,
            self.red_knight.name: self.red_knight.hp,
        }
