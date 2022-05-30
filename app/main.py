from app.game_mechanics.battle import battle
from app.game_mechanics import battle_preparation
# from app.npc.knights import fighters


battle_preparation.armour_preparation()
battle_preparation.potion_preparation()
battle_preparation.arming()

battle()
