from app.knight import Knight


class Battle:
    @staticmethod
    def battle(enemy1: Knight, enemy2: Knight) -> None:
        print(f"\n\nBattle {enemy1.name} VS {enemy2.name}")

        enemy1_damage = max(0, enemy2.power - enemy1.armour)
        enemy2_damage = max(0, enemy1.power - enemy2.armour)

        enemy1.hp -= enemy1_damage
        enemy2.hp -= enemy2_damage

        print(f"\n{enemy1.name} got {enemy1_damage} "
              f"damage from {enemy2.name}.")
        print(f"{enemy2.name} got {enemy2_damage} "
              f"damage from {enemy1.name}.\n")

        if enemy1.hp <= 0:
            enemy1.hp = 0
            print(f"{enemy1.name} has fallen!")

        if enemy2.hp <= 0:
            enemy2.hp = 0
            print(f"{enemy2.name} has fallen!")

    @staticmethod
    def tournament_result(knights: list[Knight]) -> dict:
        results = {}
        for knight in knights:
            results[knight.name] = knight.hp

        print("Tournament Results:")
        for name, hp in results.items():
            print(f"{name}: {hp} HP")

        return results
