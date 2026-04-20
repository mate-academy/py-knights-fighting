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
        self.knight_a = self._ensure_knight(knight_a)
        self.knight_b = self._ensure_knight(knight_b)

    def fight(self) -> dict:
        dmg_to_a = max(0, self.knight_b.power - self.knight_a.protection)
        dmg_to_b = max(0, self.knight_a.power - self.knight_b.protection)

        self.knight_a.receive_damage(dmg_to_a)
        self.knight_b.receive_damage(dmg_to_b)

        return {
            self.knight_a.name: max(0, int(self.knight_a.hp)),
            self.knight_b.name: max(0, int(self.knight_b.hp)),
        }
