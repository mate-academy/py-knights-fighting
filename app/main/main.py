from app.weapon.weapon import Weapon
from app.armour.armour import Armour
from app.battle.battle import Battle
from app.knight.knight import Knight
from app.potion.potion import Potion
from app.potion.effect import Effect
from knights import KNIGHTS


def create_knight(knight_data: dict) -> Knight:
    weapon_data = knight_data["weapon"]
    weapon = Weapon(name=weapon_data["name"], power=weapon_data["power"])

    knight = Knight(name=knight_data["name"],
                    power=knight_data["power"],
                    hp=knight_data["hp"],
                    weapon=weapon)

    for armour_data in knight_data["armour"]:
        armour = Armour(part=armour_data["part"],
                        protection=armour_data["protection"])
        knight.equip_armour(armour)

    potion_data = knight_data.get("potion")

    if potion_data:
        effect_data = potion_data["effect"]
        power = effect_data.get("power", 0)
        hp = effect_data.get("hp", 0)
        protection = effect_data.get("protection", 0)

        effect = Effect(power=power, hp=hp, protection=protection)
        potion = Potion(potion_data["name"], effect)
        knight.equip_potion(potion)

    return knight


def main() -> None:
    lancelot = create_knight(KNIGHTS["lancelot"])
    arthur = create_knight(KNIGHTS["arthur"])
    mordred = create_knight(KNIGHTS["mordred"])
    red_knight = create_knight(KNIGHTS["red_knight"])

    first_battle = Battle(first_knight=lancelot, second_knight=arthur)
    first_battle_result = first_battle.combat()
    print(f"First battle result: {first_battle_result}")

    second_battle = Battle(first_knight=mordred, second_knight=red_knight)
    second_battle_result = second_battle.combat()
    print(f"Second battle result: {second_battle_result}")


if __name__ == "__main__":
    main()
