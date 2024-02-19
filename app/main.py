from app.knights.knights_templates import KNIGHTS
from app.battles.battle_preparing import battle
from app.battle_process.fighting_club import fight_knights

print(fight_knights(battle(KNIGHTS)))
