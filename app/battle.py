from app.knight import Knight


class Battle:
    def __init__(self, knights: list[Knight]) -> None:
        self.first = knights[0]
        self.second = knights[1]

    @staticmethod
    def _calculate_damage(attacker: Knight, defender: Knight) -> int:
        return max(attacker.get_power() - defender.get_protection(), 0)

    def _duel(self) -> None:
        damage_to_first = self._calculate_damage(
            attacker=self.second, defender=self.first
        )

        damage_to_second = self._calculate_damage(
            attacker=self.first, defender=self.second
        )

        self.first.take_damage(damage_to_first)
        self.second.take_damage(damage_to_second)

    def run_duel(self, rounds: int = 1, until_die: bool = False) -> dict:
        if until_die:
            while not self._is_duel_over():
                self._duel()
        else:
            for _ in range(rounds):
                if self._is_duel_over():
                    break
                self._duel()

        return self._get_results()

    def _get_results(self) -> dict:
        return {
            self.first.name: self.first.get_hp(),
            self.second.name: self.second.get_hp(),
        }

    def _is_duel_over(self) -> bool:
        return not (self.first.is_alive and self.second.is_alive)
