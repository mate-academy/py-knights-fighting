from app.knights_info.characters_list import create_char, KNIGHTS
from app.battle.battle_logic import battle

# Create class instances
knights = create_char(KNIGHTS)

# Start battle
first_battle = battle([knights["lancelot"], knights["mordred"]])
second_battle = battle([knights["arthur"], knights["red_knight"]])

print(first_battle | second_battle)
