from app.models.equipment import Armor, Weapon
from app.models.knight import Knight
from app.models.potion import Potion


def conduct_battle(player: Knight, enemy: Knight) -> None:
    """Conduct a battle between player and enemy."""
    player.take_damage(enemy.power)
    enemy.take_damage(player.power)


def battle(knights_config: dict) -> dict:
    """Conduct battles between knights based on the provided configuration."""

    knights = {}
    for key, config in knights_config.items():
        knights[key] = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armor=[Armor(
                part=armor["part"],
                protection=armor["protection"])
                for armor in config["armour"]
            ],
            weapon=Weapon(
                name=config["weapon"]["name"],
                power=config["weapon"]["power"]
            ),
            potion=Potion(
                name=config["potion"]["name"],
                effect=config["potion"]["effect"]
            ) if config["potion"] else None
        )

    # Prepare knights for battle
    for knight in knights.values():
        knight.prepare_for_battle()

    # Conduct battles
    conduct_battle(knights["lancelot"], knights["mordred"])
    conduct_battle(knights["arthur"], knights["red_knight"])

    # Return battle results
    return {knight.name: knight.hp for knight in knights.values()}
