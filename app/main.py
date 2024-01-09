from typing import Dict
from app.knights import Knight

def conduct_battle(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)

def battle(knights_config: Dict[str, Knight]) -> Dict[str, int]:
    for knight_name, knight in knights_config.items():
        knight.apply_effects()

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for knight1_name, knight2_name in battles:
        conduct_battle(knights_config[knight1_name], knights_config[knight2_name])

    return {knight.name: knight.hp for knight in knights_config.values()}

# Instantiate knights using Knight class
lancelot = Knight(name="Lancelot", power=35, hp=100, weapon={"name": "Metal Sword", "power": 50})
arthur = Knight(name="Arthur", power=45, hp=75, armour=[{"part": "helmet", "protection": 15}, {"part": "breastplate", "protection": 20}, {"part": "boots", "protection": 10}], weapon={"name": "Two-handed Sword", "power": 55})
mordred = Knight(name="Mordred", power=30, hp=90, armour=[{"part": "breastplate", "protection": 15}, {"part": "boots", "protection": 10}], weapon={"name": "Poisoned Sword", "power": 60}, potion={"name": "Berserk", "effect": {"power": +15, "hp": -5, "protection": +10}})
red_knight = Knight(name="Red Knight", power=40, hp=70, armour=[{"part": "breastplate", "protection": 25}], weapon={"name": "Sword", "power": 45}, potion={"name": "Blessing", "effect": {"hp": +10, "power": +5}})

# Create knights_config dictionary
knights_config = {
    "lancelot": lancelot,
    "arthur": arthur,
    "mordred": mordred,
    "red_knight": red_knight,
}

# Run the battle
battle_results = battle(knights_config)

# Print the results
for knight_name, hp in battle_results.items():
    print(f"{knight_name}: {hp} HP")
