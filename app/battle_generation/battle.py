from app.dict_character.battle_person import Knight
from typing import Union, Tuple


def _normalize(entity: dict) -> Tuple[str, dict]:
    if isinstance(entity, Knight):
        return entity.name, entity.to_stats()
    name = entity.get("name") or "Unknown"
    stats = {
        "hp": entity.get("hp", 0),
        "power": entity.get("power", 0),
        "protection": entity.get("protection", 0),
    }
    return name, stats


def _dict_to_knight(data: Knight) -> Knight:
    name = data.get("name", "Unknown")
    power = data.get("power", 0)
    hp = data.get("hp", 0)
    armour = data.get("armour") or []
    weapon = data.get("weapon")
    potion = data.get("potion")
    return Knight(
        name=name,
        power=power,
        hp=hp,
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


class Battle:
    def generate_battle(self, entity_a: Union[dict, Knight],
                        entity_b: Union[dict, Knight]) -> dict:
        if isinstance(entity_a, dict):
            entity_a = _dict_to_knight(entity_a)
        if isinstance(entity_b, dict):
            entity_b = _dict_to_knight(entity_b)
        name_a, stat_a = _normalize(entity_a)
        name_b, stat_b = _normalize(entity_b)
        power_a = stat_a.get("power", 0)
        prot_a = stat_a.get("protection", 0)
        hp_a = stat_a.get("hp", 0)
        power_b = stat_b.get("power", 0)
        prot_b = stat_b.get("protection", 0)
        hp_b = stat_b.get("hp", 0)
        damage_to_a = max(0, power_b - prot_a)
        damage_to_b = max(0, power_a - prot_b)
        new_hp_a = max(0, hp_a - damage_to_a)
        new_hp_b = max(0, hp_b - damage_to_b)
        return {name_a: new_hp_a, name_b: new_hp_b}
