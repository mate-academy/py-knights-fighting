from app.knight.knight import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


def knights_builder(knights_config: dict, knight: str) -> Knight:
    armour_items = knights_config.get("armour") or []
    return Knight(
        knights_config.get("name"),
        knights_config.get("hp"),
        knights_config.get("power"),
        [
            Armour(item.get("part"), item.get("protection"))
            for item in armour_items
        ],
        Weapon(
            knights_config.get("weapon").get("name"),
            knights_config.get("weapon").get("power"),
        ),
        Potion(
            knights_config.get("potion").get("name"),
            knights_config.get("potion").get("effect"),
        ) if knights_config.get("potion") is not None else None,
    )
