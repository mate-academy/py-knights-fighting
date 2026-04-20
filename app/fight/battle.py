from app.models.knight import Knight


class Battle:
    @staticmethod
    def _ensure_knight(raw_or_knight: Knight | dict) -> Knight:
        if isinstance(raw_or_knight, Knight):
            knight = raw_or_knight
        else:
            knight = Knight(raw_or_knight)
        knight.prepare()
        return knight

    def __init__(self, knight_a: Knight | dict,
                 knight_b: Knight | dict) -> None:
        self.a = self._ensure_knight(knight_a)
        self.b = self._ensure_knight(knight_b)

    def fight(self) -> dict:
        dmg_to_a = max(0, self.b.power - self.a.protection)
        dmg_to_b = max(0, self.a.power - self.b.protection)

        self.a.receive_damage(dmg_to_a)
        self.b.receive_damage(dmg_to_b)

        return {
            self.a.name: max(0, int(self.a.hp)),
            self.b.name: max(0, int(self.b.hp)),
        }
