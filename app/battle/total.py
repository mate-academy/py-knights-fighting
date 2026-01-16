from app.preparations.weapon import Weapon
from app.preparations.armor import Armor
from app.preparations.health import Health


class Score:
    def __init__(self, info_1: dict, info_2: dict) -> None:
        self.info_1 = info_1
        self.info_2 = info_2

    def get_score(self) -> int:
        result = (
            Health(self.info_1).get_hp()
            - (Weapon(self.info_2).get_power()
               - Armor(self.info_1).protection())
        )
        if result <= 0:
            result = 0
        return result
