from app.fighters.knight import Knight


class Perk:
    @staticmethod
    def apply_armour(knight: Knight) -> None:
        armour_effect = 0
        for part in knight.armour:
            armour_effect += part["protection"]

        knight.protection += armour_effect
        if armour_effect != 0:
            print(f"+ armour effect: {armour_effect} protection")

    @staticmethod
    def apply_weapon(knight: Knight) -> None:
        weapon_effect = knight.weapon["power"]
        knight.power += weapon_effect
        if weapon_effect != 0:
            print(f"+ weapon effect: {weapon_effect} power")

    @staticmethod
    def apply_potion(knight: Knight) -> None:
        if knight.potion is not None:
            potion_effects_result = []
            for effect, value in knight.potion["effect"].items():
                if effect in ("power", "hp", "protection"):
                    setattr(knight, effect, getattr(knight, effect) + value)
                    potion_effects_result.append(f"+ {effect}: {value}")
            print("potion effects: " + ", ".join(potion_effects_result))

    @staticmethod
    def apply_all_perks(knight: Knight) -> None:
        print(knight.name.upper(), "applied perks:")
        Perk.apply_armour(knight)
        Perk.apply_weapon(knight)
        Perk.apply_potion(knight)
        print("---")
