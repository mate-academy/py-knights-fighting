from app.domain.registry import Loadout

lancelot_loadout = Loadout(
    weapon_id = "metal_sword",
    armour_ids = [],
    potion_id = None
)

arthur_loadout = Loadout(
    weapon_id = "two_handed_sword",
    armour_ids = ["helmet", "breastplate_20", "boots"],
    potion_id = None
)

mordred_loadout = Loadout(
    weapon_id = "poisoned_sword",
    armour_ids = ["breastplate_15", "boots"],
    potion_id = "berserk"
)

red_knight_loadout = Loadout(
    weapon_id = "sword",
    armour_ids = ["breastplate_25"],
    potion_id = "blessing"
)