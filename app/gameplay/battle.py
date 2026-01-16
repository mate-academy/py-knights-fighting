from app.characters.knight import Knight


class Battle:
    def __init__(self, battles: list) -> None:
        self.battles = [
            (
                Knight.knights.get(knight_alias[0]),
                Knight.knights.get(knight_alias[1])
            )
            for knight_alias in battles
        ]

    @staticmethod
    def perform_duel(knight1: Knight, knight2: Knight) -> None:
        damage_knight1 = max(0, knight2.effective_power() - knight1.protection)
        damage_knight2 = max(0, knight1.effective_power() - knight2.protection)

        knight1.take_damage(damage_knight1)
        knight2.take_damage(damage_knight2)

    def conduct_battle(self) -> dict:

        for knight1, knight2 in self.battles:
            knight1.prepare_for_battle()
            knight2.prepare_for_battle()

            # Duel
            self.perform_duel(knight1, knight2)

        # Return battle results:
        return {knight.name: knight.hp for knight in Knight.knights.values()}
