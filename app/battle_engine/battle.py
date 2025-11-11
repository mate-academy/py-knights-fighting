from app.models import Knight
from typing import Dict, Optional


class Battle:
    def __init__(self, knight1 : Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2
        self._battle_occurred = False

    def fight(self) -> Dict[str, int]:
        self._battle_occurred = True

        damage_to_knight1 = self.knight2.power - self.knight1.protection
        damage_to_knight2 = self.knight1.power - self.knight2.protection

        self.knight1.take_damage(max(0, damage_to_knight1))
        self.knight2.take_damage(max(0, damage_to_knight2))

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp
        }

    def get_winner(self) -> Optional[Knight]:
        if not self._battle_occurred:
            return None

        if self.knight1.hp > 0 and self.knight2.hp > 0:
            return None
            return self.knight1
        elif self.knight2.hp > 0:
            return self.knight2
        else:
            return None

    def is_battle_over(self) -> bool:
        if not self._battle_occurred:
            return False
        return self.knight1.is_defeated() or self.knight2.is_defeated()

    def __repr__(self) -> str:
        status = "Not started" if not self._battle_occurred else "Completed"
        return f"Battle({self.knight1.name} vs {self.knight2.name}) - {status}"
