from app.knight.knight import Knight
from app.weapon.weapon import Weapon
from app.armour.armour import Armour
from app.potion.potion import Potion
from app.potion.effect import Effect
from app.battle.battle import Battle


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
    for key, knight_config in knights_config.items():
        knights[key] = create_knight(knight_config)

    battle_results = {}
    for i in range(0, 2):
        if i == 0:
            battle_obj = Battle(knights["lancelot"], knights["mordred"])
        else:
            battle_obj = Battle(knights["arthur"], knights["red_knight"])

        battle_results.update(battle_obj.fight())

    return battle_results
