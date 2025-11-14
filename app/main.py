from app.people.knights_data import KNIGHTS
from app.actions.register import register_knights
from app.actions.battle import battle

registered_knights = register_knights(KNIGHTS)

print(battle(registered_knights))
