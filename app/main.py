from .knight.knight import Knight
from .weapon.weapon import Weapon
from .armour.armour import Armour
from .potion.potion import Potion
from .potion.effect import Effect
from .battle.battle import Battle


def create_knight(knight_config: dict) -> Knight:
    weapon = Weapon(
        knight_config["weapon"]["name"],
        knight_config["weapon"]["power"]
    )

    knight = Knight(
        name=knight_config["name"],
        power=knight_config["power"],
        hp=knight_config["hp"],
        weapon=weapon
    )

    for armour in knight_config["armour"]:
        knight.add_armour(Armour(armour.get("part"), armour.get("protection")))

    if knight_config["potion"]:
        effect = Effect(
            knight_config["potion"]["effect"].get("power", 0),
            knight_config["potion"]["effect"].get("hp", 0),
            knight_config["potion"]["effect"].get("protection", 0)
        )
        potion = Potion(
            knight_config["potion"]["name"],
            effect
        )

        knight.set_potion(potion)

    return knight


def battle(knights_config: dict) -> dict:
    knights = {}
    for knight_alias, knight_config in knights_config.items():
        knights[knight_alias] = create_knight(knight_config)

    knight_pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    battle_results = {}
    for knight1, knight2 in knight_pairs:
        battle_obj = Battle(knights.get(knight1), knights.get(knight2))
        battle_results.update(battle_obj.fight())

    return battle_results
