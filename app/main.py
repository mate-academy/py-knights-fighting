from app.stats import KNIGHTS
from app.arenas.camelot import Camelot
from app.knights.knight import Knight

def battle(knightsConfig):
    battle_arena = Camelot()
    knights = [
        Knight(name=knight["name"],
               hp=knight["hp"],
               power=knight["power"],
               armour=knight["armour"],
               weapon=knight["weapon"],
               potion=knight["potion"])
               for knight in knightsConfig.values()
        ]

    battle_arena.knight_battle(knight_one=knights[0].prepare_for_battle(),
                               knight_two=knights[1].prepare_for_battle())
    battle_arena.knight_battle(knight_one=knights[2].prepare_for_battle(),
                               knight_two=knights[3].prepare_for_battle())

    return battle_arena.battles_result_on_arena

print(battle(KNIGHTS))