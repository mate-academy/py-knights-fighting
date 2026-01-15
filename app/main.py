class Knight:
    def __init__(self, name, power, hp, armour=None, weapon=None, potion=None):
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour if armour else []
        self.weapon = weapon
        self.potion = potion
        self.final_stats = self._calculate_stats()

    def _calculate_stats(self):
        final_power = self.base_power
        final_hp = self.base_hp
        final_protection = 0

        # Додаємо захист від броні
        for piece in self.armour:
            final_protection += piece.get("protection", 0)

        # Додаємо силу від зброї
        if self.weapon:
            final_power += self.weapon.get("power", 0)

        # Додаємо ефекти зілля
        if self.potion:
            effect = self.potion.get("effect", {})
            final_power += effect.get("power", 0)
            final_hp += effect.get("hp", 0)
            final_protection += effect.get("protection", 0)

        return {
            "power": final_power,
            "hp": final_hp,
            "protection": final_protection,
        }

    def attack(self, other):
        damage = max(0, self.final_stats["power"] - other.final_stats["protection"])
        other.final_stats["hp"] -= damage
        return damage


def simulate_battle(knight1, knight2):

    round_counter = 1
    while knight1.final_stats["hp"] > 0 and knight2.final_stats["hp"] > 0:
        print(f"Round {round_counter}: {knight1.name} attacks {knight2.name}!")
        damage = knight1.attack(knight2)
        print(f"{knight1.name} deals {damage} damage. {knight2.name} has {knight2.final_stats['hp']} HP left.")

        if knight2.final_stats["hp"] <= 0:
            print(f"{knight1.name} wins!")
            return {"winner": knight1.name, "loser": knight2.name}

        print(f"Round {round_counter}: {knight2.name} attacks {knight1.name}!")
        damage = knight2.attack(knight1)
        print(f"{knight2.name} deals {damage} damage. {knight1.name} has {knight1.final_stats['hp']} HP left.")

        if knight1.final_stats["hp"] <= 0:
            print(f"{knight2.name} wins!")
            return {"winner": knight2.name, "loser": knight1.name}

        round_counter += 1

    return {"winner": None, "loser": None}  # У разі нічиєї


def main():
    KNIGHTS_CONFIG = {
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
                {"part": "boots", "protection": 10},
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
                {"part": "boots", "protection": 10},
            ],
            "weapon": {"name": "Poisoned Sword", "power": 60},
            "potion": {"name": "Berserk", "effect": {"power": 15, "hp": -5, "protection": 10}},
        },
        "red_knight": {
            "name": "Red Knight",
            "power": 40,
            "hp": 70,
            "armour": [{"part": "breastplate", "protection": 25}],
            "weapon": {"name": "Sword", "power": 45},
            "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
        },
    }

    # Створюємо лицарів
    knights = {
        name: Knight(
            data["name"], data["power"], data["hp"], data.get("armour"), data["weapon"], data.get("potion")
        )
        for name, data in KNIGHTS_CONFIG.items()
    }

    # Битва
    result1 = simulate_battle(knights["lancelot"], knights["mordred"])
    result2 = simulate_battle(knights["arthur"], knights["red_knight"])

    # Вивід результатів
    battle_results = {"battle_1": result1, "battle_2": result2}
    print("Final Results:", battle_results)


if __name__ == "__main__":
    main()
