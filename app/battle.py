from __future__ import annotations
from app.armour import Armour
from app.knights import Knights
from app.potion import Potion
from app.weapon import Weapon


def battle(knights: dict) -> dict[str, int]:
    def create_knight_from_dict(knight_data: dict) -> Knights:
        armour = [Armour(a["part"],
                         a["protection"]) for a
                  in knight_data.get("armour", [])]
        weapon_data = knight_data.get("weapon")
        weapon = Weapon(weapon_data["name"],
                        weapon_data["power"]) if weapon_data else None
        potion_data = knight_data.get("potion")
        potion = Potion(potion_data["name"],
                        potion_data["effect"]) if potion_data else None
        return Knights(knight_data["name"],
                       knight_data["power"],
                       knight_data["hp"],
                       armour=armour,
                       weapon=weapon,
                       potion=potion)

    knight1 = create_knight_from_dict(knights["lancelot"])
    knight2 = create_knight_from_dict(knights["mordred"])
    knight3 = create_knight_from_dict(knights["arthur"])
    knight4 = create_knight_from_dict(knights["red_knight"])

    # Battle
    knight1.prepare_for_battle()
    knight2.prepare_for_battle()
    knight3.prepare_for_battle()
    knight4.prepare_for_battle()

    # Lancelot & Mordred
    knight1.hp -= max(0, knight2.power - knight1.protection)
    knight2.hp -= max(0, knight1.power - knight2.protection)

    # Arthur & Red Knight
    knight3.hp -= max(0, knight4.power - knight3.protection)
    knight4.hp -= max(0, knight3.power - knight4.protection)

    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)
    knight3.hp = max(0, knight3.hp)
    knight4.hp = max(0, knight4.hp)

    # Battle result
    return {knight1.name: knight1.hp,
            knight2.name: knight2.hp,
            knight3.name: knight3.hp,
            knight4.name: knight4.hp}
