import time


from app.knights import Knight


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10}
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10}
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {
            "name": "Berserk",
            "effect": {"power": +15, "hp": -5, "protection": +10}
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": +10, "power": +5}
        }
    }
}


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot.take_damage(mordred)
    mordred.take_damage(lancelot)
    arthur.take_damage(red_knight)
    red_knight.take_damage(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


def duel_round(k1: Knight, k2: Knight) -> Knight:
    print(f"\nBATTLE: {k1.name} VS {k2.name}")

    while k1.hp > 0 and k2.hp > 0:

        old_hp2 = k2.hp
        k2.take_damage(k1)
        damage_to_k2 = old_hp2 - k2.hp
        print(f"{k1.name} deals {damage_to_k2} damage. {k2.name} HP: {k2.hp}")
        time.sleep(0.5)

        if k2.hp <= 0:
            print(f"{k2.name} has fallen. {k1.name} wins!")
            return k1

        old_hp1 = k1.hp
        k1.take_damage(k2)
        damage_to_k1 = old_hp1 - k1.hp
        print(f"{k2.name} deals {damage_to_k1} damage. {k1.name} HP: {k1.hp}")
        time.sleep(0.5)

        if k1.hp <= 0:
            print(f"{k1.name} has fallen. {k2.name} wins!")
            return k2

    return k1 if k1.hp > 0 else k2


def duel(knights_config: dict) -> Knight:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    winners = []

    print("--- FIRST ROUND ---")
    winners.append(duel_round(lancelot, mordred))
    winners[0].heal()

    print("\n--- SECOND ROUND ---")
    winners.append(duel_round(arthur, red_knight))
    winners[1].heal()

    print("\n--- FINAL ROUND ---")
    print(f"FINALISTS: {winners[0].name} vs {winners[1].name}")

    champion = duel_round(winners[0], winners[1])
    champion.heal()

    print(f"\nTOURNAMENT CHAMPION: {champion.name.upper()}")
    return champion


if __name__ == "__main__":
    duel(KNIGHTS)
