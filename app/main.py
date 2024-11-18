from app.kamelot.knights_dict import KNIGHTS
from app.kamelot.knight import Knight
from app.kamelot.battle import duel, standings


knights_list = Knight.init_from_dict(KNIGHTS)

lancelot, arthur, mordred, red_knight = knights_list

first_duel_results = duel(lancelot, mordred)
second_duel_results = duel([arthur, red_knight])

results = standings(lancelot, arthur, mordred, red_knight)

print(results)
