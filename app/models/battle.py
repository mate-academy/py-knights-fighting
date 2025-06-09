from app.models.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> dict[str, int]:
        stats1 = self.knight1.calculate_stats()
        stats2 = self.knight2.calculate_stats()

        knight1_damage = (
            max(stats2["total_power"] - stats1["total_protection"], 0)
        )

        knight2_damage = (
            max(stats1["total_power"] - stats2["total_protection"], 0)
        )

        hp1 = max(stats1["total_hp"] - knight1_damage, 0)
        hp2 = max(stats2["total_hp"] - knight2_damage, 0)

        return {
            self.knight1.name: hp1,
            self.knight2.name: hp2,
        }
