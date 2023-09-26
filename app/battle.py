from typing import List, Dict

from app.knights import Knight


class Battle:
    def __init__(self, knights: List[Knight]) -> None:
        self.knights = knights

    def start(self) -> Dict[str, int]:
        for knight in self.knights:
            knight.initialize()

        battles = [(0, 1), (2, 3)]  # Lancelot vs Arthur, Mordred vs Red Knight

        results = {}
        for knight_index1, knight_index2 in battles:
            knight1, knight2 = self.knights[knight_index1], \
                self.knights[knight_index2]
            while knight1.hp > 0 and knight2.hp > 0:
                # Рассчитываем урон с учетом оружия и брони рыцарей
                damage1 = max(knight1.power - knight2.protection, 0)
                damage2 = max(knight2.power - knight1.protection, 0)

                # Применяем эффекты зелий (если есть) перед атакой
                if knight1.potion:
                    damage1 += knight1.potion.get("effect", {}).get("power", 0)

                if knight2.potion:
                    damage2 += knight2.potion.get("effect", {}).get("power", 0)

                # Наносим урон друг другу
                knight1.hp -= damage2
                knight2.hp -= damage1

            # Обновляем здоровье рыцарей после боя
            knight1.hp = max(knight1.hp, 0)
            knight2.hp = max(knight2.hp, 0)

            results[knight1.name] = max(knight1.hp, 0)
            results[knight2.name] = max(knight2.hp, 0)

        return results
