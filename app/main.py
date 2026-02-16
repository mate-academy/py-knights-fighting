from __future__ import annotations

from app.domain.items import Weapon, Armour, Potion
from app.domain.registry import ItemRegistry, Loadout
from app.domain.knight import Knight


def _knights_from_config(config: dict) -> dict[str, Knight]:
    weapons: dict[str, Weapon] = {}
    armours: dict[str, Armour] = {}
    potions: dict[str, Potion] = {}

    loadouts: dict[str, Loadout] = {}

    for kid, cfg in config.items():
        # weapon
        weapon_id = f"{kid}_weapon"
        weapons[weapon_id] = Weapon(
            cfg["weapon"]["name"], cfg["weapon"]["power"]
        )

        # armour
        armour_ids: list[str] = []
        for i, aa in enumerate(cfg["armour"]):
            armour_id = f"{kid}_armour_{i}"
            armours[armour_id] = Armour(aa["part"], aa["protection"])
            armour_ids.append(armour_id)

        # potion (optional)
        potion_id = None
        if cfg.get("potion") is not None:
            potion_id = f"{kid}_potion"
            pp = cfg["potion"]
            potions[potion_id] = Potion(pp["name"], pp.get("effect", {}))

        loadouts[kid] = Loadout(
            weapon_id=weapon_id,
            armour_ids=armour_ids,
            potion_id=potion_id,
        )

    registry = ItemRegistry(weapons=weapons, armours=armours, potions=potions)

    knights: dict[str, Knight] = {}
    for kid, cfg in config.items():
        knights[kid] = Knight(
            name=cfg["name"],
            hp=cfg["hp"],
            power=cfg["power"],
            protection=0,          # в тестовом dict базовой защиты нет
            registry=registry,
            equipment=loadouts[kid],
        )
    return knights


def _duel(k1: Knight, k2: Knight) -> tuple[int, int]:
    c1 = k1.apply_equipment()
    c2 = k2.apply_equipment()

    # защита вычитается у цели, урон не ниже 0
    dmg_to_c1 = max(0, c2.power - c1.protection)
    dmg_to_c2 = max(0, c1.power - c2.protection)

    c1_hp = max(0, c1.hp - dmg_to_c1)
    c2_hp = max(0, c2.hp - dmg_to_c2)
    return c1_hp, c2_hp


def battle(config: dict) -> dict[str, int]:
    knights = _knights_from_config(config)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    l_hp, m_hp = _duel(lancelot, mordred)
    a_hp, r_hp = _duel(arthur, red_knight)

    return {
        lancelot.name: l_hp,
        arthur.name: a_hp,
        mordred.name: m_hp,
        red_knight.name: r_hp,
    }
