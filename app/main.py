from app.Characters.knights import Knight


arthur = Knight(
    name="Arthur",
    base_hp=75,
    base_power=45,
    weapon={"name": "Two-handed Sword", "power": 55},
    armour=[
        {"part": "Helmet", "protection": 15},
        {"part": "Breastplate", "protection": 20},
        {"part": "Boots", "protection": 10}
    ],
    potion=None
)

arthur.prepare_to_battle()

lancelot = Knight(
    name="Lancelot",
    base_hp=35,
    base_power=100,
    weapon={"name": "Metal_sword", "power": 50},
    armour=[],
    potion=None,
)

lancelot.prepare_to_battle()

mordred = Knight(
    name="Mordred",
    base_hp=30,
    base_power=90,
    weapon={"name": "poison_sword", "power": 60},
    armour=[
        {"part": "breastplate", "protection": 25},
        {"part": "boots", "protection": 10},
    ],
    potion={
        "name": "Berserk",
        "effect": {"hp": -5, "power": +15, "protection": +20},
    }
)

mordred.prepare_to_battle()

red_knight = Knight(
    name="Red Knight",
    base_hp=40,
    base_power=70,
    weapon={"name": "sword", "power": 45},
    armour=[
        {"part": "breastplate", "protection": 25}
    ],
    potion={
        "name": "Blessing",
        "effect": {"hp": +10, "power": +5, "protection": 0},
    }
)

red_knight.prepare_to_battle()

lancelot.fight(mordred)
arthur.fight(red_knight)

print(f"{lancelot.name}: {lancelot.hp} HP")
print(f"{mordred.name}: {mordred.hp} HP")
print(f"{arthur.name}: {arthur.hp} HP")
print(f"{red_knight.name}: {red_knight.hp} HP")
