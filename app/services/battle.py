from typing import Dict, List

from app.knights.knight import Knight


class Battle:
    def __init__(self, knights: dict) -> None:
        self.knights = [Knight(**knights[knight]) for knight in knights]

    def start(self) -> Dict[str, int]:
        self.knights = self.__sort_knights()

        for i in range(0, len(self.knights) - 1, 2):
            self.knights[i] = self.__hit(
                self.knights[i], self.knights[i + 1].power
            )

            self.knights[i + 1] = self.__hit(
                self.knights[i + 1], self.knights[i].power
            )

        return {knight.name: knight.hp for knight in self.knights}

    @staticmethod
    def __hit(knight: Knight, power: int) -> Knight:
        knight.hp -= power - knight.protection

        if knight.hp < 0:
            knight.hp = 0
        return knight

    def __sort_knights(self) -> List[Knight]:
        return sum(
            [
                [self.knights[i] for i in range(k, len(self.knights), 2)]
                for k in range(2)
            ],
            []
        )
