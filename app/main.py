from app.knights.knight_stats import Knight
from app.battles.battle import perform_battle

def main():
    # Define knights
    knights = {
        "Lancelot": Knight("Lancelot", 35, 100, [], {"name": "Metal Sword", "power": 50}),
        "Arthur": Knight("Arthur", 45, 75, [{"part": "helmet", "protection": 15}], {"name": "Two-handed Sword", "power": 55}),
        "Mordred": Knight("Mordred", 30, 90, [{"part": "breastplate", "protection": 15}], {"name": "Poisoned Sword", "power": 60}, {"name": "Berserk", "effect": {"power": +15, "hp": -5, "protection": +10}}),
        "Red Knight": Knight("Red Knight", 40, 70, [{"part": "breastplate", "protection": 25}], {"name": "Sword", "power": 45}, {"name": "Blessing", "effect": {"hp": +10, "power": +5}})
    }

    # Perform battles
    lancelot_vs_mordred = battle(knights["Lancelot"], knights["Mordred"])
    arthur_vs_red_knight = battle(knights["Arthur"], knights["Red Knight"])

    # Print results
    print("Lancelot vs Mordred:", lancelot_vs_mordred)
    print("Arthur vs Red Knight:", arthur_vs_red_knight)

if __name__ == "__main__":
    main()
