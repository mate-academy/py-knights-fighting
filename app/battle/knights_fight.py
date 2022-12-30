from app.knights.prepare_to_battle import KnightsPrepareToBattle


class BattleRound:

    @staticmethod
    def knights_battle_result(
            first_knight: KnightsPrepareToBattle,
            second_knight: KnightsPrepareToBattle
    ) -> dict:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        first_knight.check_hp_after_battle()
        second_knight.check_hp_after_battle()

        return {
            first_knight.name: first_knight.hp,
            second_knight.name: second_knight.hp,
        }
