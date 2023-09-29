from app.battle import Battle
from app.knights_list import KNIGHTS

battle_instance = Battle(KNIGHTS)
battle_instance.apply_knight_modifiers()
results = battle_instance.fight()
print(results)

def battle(KnightConfig):