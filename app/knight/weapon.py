from app.knight.knight import Knight


def to_arm_armour(armors: list[dict]) -> int:
    return sum([armor.get("protection") for armor in armors])


def to_arm_weapon(weapon: dict) -> int:
    return weapon.get("power")


def to_arm_potion(potion: dict, knight: Knight) -> Knight:
    if potion:
        for characteristic, num in potion.get("effect", {}).items():
            if hasattr(knight, characteristic):
                setattr(
                    knight,
                    characteristic,
                    getattr(knight, characteristic) + num)

    return knight
