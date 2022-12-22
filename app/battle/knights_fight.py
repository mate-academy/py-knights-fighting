from app.knights.prepare_to_battle import KnightsPrepareToBattle


class BattleRound:

    @staticmethod
    def knights_battle_result(first_knight: KnightsPrepareToBattle,
                              second_knight: KnightsPrepareToBattle
                              ) -> dict:

        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        if first_knight.hp <= 0:
            first_knight.hp = 0

        if second_knight.hp <= 0:
            second_knight.hp = 0

        return {
            first_knight.name: first_knight.hp,
            second_knight.name: second_knight.hp,
        }
