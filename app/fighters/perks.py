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
        potion_effects_result = "potion effects: "
        if knight.potion is not None:
            potion_effects = knight.potion["effect"]
            for effect, value in potion_effects.items():
                if effect == "power":
                    knight.power += value
                    potion_effects_result += f"+ power: {value}, "
                if effect == "hp":
                    knight.hp += value
                    potion_effects_result += f"+ hp: {value}, "
                if effect == "protection":
                    knight.protection += value
                    potion_effects_result += f"+ protection: {value} "
            print(f"{potion_effects_result}")

    @staticmethod
    def apply_all_perks(knight: Knight) -> None:
        print(knight.name.upper(), "applied perks:")
        Perk.apply_armour(knight)
        Perk.apply_weapon(knight)
        Perk.apply_potion(knight)
        print("---")
