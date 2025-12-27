from app.prepare_to_battle.knight_damage import knight_weapon
from app.prepare_to_battle.knight_protection import armor_protection
from app.prepare_to_battle.knight_hp import hp


class IsReady:

    def __init__(self, knight_stats: dict) -> None:
        self.knight_stats = knight_stats

    def is_ready(self) -> dict:
        return {
            "name": self.knight_stats["name"],
            "hp": hp(self.knight_stats),
            "power": knight_weapon(self.knight_stats),
            "protection": armor_protection(self.knight_stats)
        }
