from app.knights.basic_stats import knights_instances_dict
from app.knights.prepare_to_battle import KnightsPrepareToBattle


def knights_get_ready_to_battle(knights_dict: dict) -> dict:
    knights_instances = knights_instances_dict(knights_dict)
    final_knights_stats = {}

    for knight_name, knight_stats in knights_instances.items():
        final_knights_stats[knight_name] = KnightsPrepareToBattle(knight_stats)
        final_knights_stats[knight_name].apply_armour(knight_stats)
        final_knights_stats[knight_name].apply_weapon(knight_stats)
        final_knights_stats[knight_name].apply_potion(knight_stats)

    return final_knights_stats
